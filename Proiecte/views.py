from django.shortcuts import render
from .models import *

def esu(request):
    return render(request, 'esu.html')

def etf(request):
    return render(request, 'etf.html')

def exchange(request):
    return render(request, 'exchange.html')

def ftfmm(request):
    return render(request, 'ftfmm.html')

def masarotunda(request):
    return render(request, 'masarotunda.html')

def new(request):
    return render(request, 'new.html')

# Create your views here.
