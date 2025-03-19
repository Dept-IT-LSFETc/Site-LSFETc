from django.urls import path
from . import views as v

urlpatterns = [
    path('esu', v.esu),
    path('etf', v.etf),
    path('exchange', v.exchange),
    path('ftfmm', v.ftfmm),
    path('masarotunda', v.masarotunda),
    path('new', v.new),
]