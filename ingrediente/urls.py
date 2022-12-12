from django.urls import path 
from ingrediente.views import ingrediente,ingrediente_crear

urlpatterns = [
  path('',ingrediente,name="ingrediente"), 
  path('crear/',ingrediente_crear,name="ingrediente-crear"),
]
