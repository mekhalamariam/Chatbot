from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'Auth/login.html')


def signup(request):
    return render(request, 'Auth/signup.html')
