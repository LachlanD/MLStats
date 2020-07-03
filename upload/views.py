from django.shortcuts import render
from upload.models import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

def load(request):
    return render(request, 'load.html')

def summary(request):
    return render(request, 'summary.html')
