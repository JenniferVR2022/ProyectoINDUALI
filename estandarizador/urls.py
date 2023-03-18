from django.urls import path 
from estandarizador.views import estandarizador,agregar_receta

urlpatterns = [
  path('',estandarizador,name="estandarizador"), 
  path('agregar/',agregar_receta,name="agregar-receta"),
]