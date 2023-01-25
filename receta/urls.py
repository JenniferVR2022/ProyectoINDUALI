from django.urls import path
from receta.views import receta,receta_crear

urlpatterns = [
    path('',receta,name="receta"),
    path('crear/',receta_crear,name="receta-crear"),
]