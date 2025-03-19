from django.urls import path
from . import views as v

urlpatterns = [
    path('lsfetc', v.lsfetc),
    path('bc', v.bc),
    path('galerie', v.galerie),
    path('departamente', v.departamente),
]