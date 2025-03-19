from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    pozaprincipala = Pagina_Principala_PozaPrincipala.objects.order_by('index')
    OrganizatiiPartenere = Pagina_Principala_OrganizatiiPartenere.objects.order_by('index')
    testimoniale = Pagina_Principala_Testimoniale.objects.order_by('index')
    nr = Pagina_Principala_Numere.objects.order_by('index')
    return render (request, 'acasa.html', {'pozaprincipala' : pozaprincipala, 'OrganizatiiPartenere' : OrganizatiiPartenere , 'testimoniale' : testimoniale, 'numere' : nr,})



def faq(request):
    return render (request,'faq.html')


def anunturi(request):
    return render(request, 'anunturi.html')

def contact(request):
    contact = Contact_Persoane_de_contact.objects.order_by('index')
    return render(request, 'contact.html', {'contact': contact,})