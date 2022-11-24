from django.urls import path 
from ingrediente.views import ingrediente,ingrediente_buscar

urlpatterns = [
  path('',ingrediente,name="ingrediente"), 
  path('buscar/',ingrediente_buscar,name="ingrediente-buscar"),
]



