from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse

from sondage.models import Question, Choice

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('sondage/index.html')
    context = {'latest_question_list': latest_question_list}
    return HttpResponse(template.render(context, request))

@login_required(login_url='/accounts/login/')
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'sondage/detail.html', {'question': question})

@login_required(login_url='/accounts/login/')
def vote (request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'sondage/detail.html', {'question': question, 'error_message':"Vous n'avez pas selectioné un choix" })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('sondage:results', args=(question.id,)))

@login_required(login_url='/accounts/login/')
def results (request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'sondage/results.html', {'question':question})