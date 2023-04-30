from django.urls import path
from receta.views import receta,receta_crear,receta_agregar

urlpatterns = [
    path('',receta,name="receta"),
    path('crear/',receta_crear,name="crear-receta"),
    path('agregar/',receta_agregar,name="receta-agregar"),
]