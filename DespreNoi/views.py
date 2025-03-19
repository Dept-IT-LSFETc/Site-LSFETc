from django.shortcuts import render
from .models import *

def lsfetc(request):
    return render (request, 'lsfetc.html')

def bc(request):
    poza = Desprenoi_BC_PozaCoperta_si_text.objects.all()
    biroul_executiv = Desprenoi_BC_Biroul_executiv.objects.order_by('index')
    coordonatori = Desprenoi_BC_Coordonatori_Departamente.objects.order_by('index')
    comisia = Desprenoi_BC_Comisia_de_cenzori.objects.order_by('index')
    return render (request, 'bc.html', {'poza' : poza, 'bex':biroul_executiv, 'bc' : coordonatori, 'cc' : comisia,})

def departamente(request):
    return render (request, 'departamente.html')

def galerie(request):
    return render (request, 'galerie.html')

# Create your views here.
