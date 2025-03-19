from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blog.html')

def documente(request):
    return render(request, 'documente.html')

def proiectevechi(request):
    return render(request, 'proiectevechi.html')

def studenti(request):
    return render(request, 'studentii.html')