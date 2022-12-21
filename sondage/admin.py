from django.contrib import admin

from sondage.models import Question, Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
