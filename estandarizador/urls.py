from django.urls import path 
from estandarizador.views import estandarizador,agregar_receta,lista_centrocostos

urlpatterns = [
  path('',estandarizador,name="estandarizador"), 
  path('agregar/',agregar_receta,name="agregar-receta"),
  path('listar/',lista_centrocostos,name="lista-centrocostos"),

]