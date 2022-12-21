from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from sondage.models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('sondage/index.html')
    context = {'latest_question_list': latest_question_list}
    return HttpResponse(template.render(context, request))

def detail(resuest, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(resuest, 'sondage/detail.html', {'question': question})