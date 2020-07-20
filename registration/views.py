from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import CoachSignUpForm
from .models import User,Coach
# Create your views here.

def index(request):
    return HttpResponse('hello')


class CoachRegistration(CreateView):
    template_name = 'index.html'
    model = User
    form_class = CoachSignUpForm

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        # Will uncomment this for later
        # login(self.request, user)
        return redirect('/')

