from django.http import HttpResponse
from django.template import RequestContext, loader

from django.shortcuts import render, render_to_response

# from discipline.models import Event


def index(request):
  context = {
#     'mood_initial': Event.objects.all()[0].mood
  }
  return render(request, 'discipline_app/index.html', context)
