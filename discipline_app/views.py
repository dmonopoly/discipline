from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.contrib import messages
from forms import *

from django.shortcuts import render, render_to_response


def index(request):
  context = {
#     'mood_initial': Event.objects.all()[0].mood
  }
  return render(request, 'discipline_app/index.html', context)

def signup(request):
  if request.method == 'POST':
    form = UserCreateForm(request.POST)
    if form.is_valid():
      user = form.save()
      user.save()
      messages.success(request, 'Signup successful.')
      return HttpResponseRedirect('/')
  else:
    form = UserCreateForm()
  return render(request, 'discipline_app/signup.html', {
    'form': form,
  })

