from django.urls import path 
from listaPrecio.views import listaPrecio,listap_crear

urlpatterns = [
  path('',listaPrecio,name="listaPrecio"),
  path('crear/',listap_crear,name="listap-crear"),
]


    