from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse, Http404
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')
