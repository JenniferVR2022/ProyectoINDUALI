from django.urls import path
from receta.views import receta

urlpatterns = [
    path('',receta,name="receta"),

]