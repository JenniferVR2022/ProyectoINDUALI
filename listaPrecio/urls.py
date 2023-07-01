from django.urls import path 
from listaPrecio.views import listaPrecio,listap_crear,editar

urlpatterns = [
  path('',listaPrecio,name="listaPrecio"),
  path('crear/',listap_crear,name="listap-crear"),
  path('editar/<int:id>', editar, name="editar-LP"),
]


    