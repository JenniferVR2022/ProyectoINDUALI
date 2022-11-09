from django.urls import path
from ListaPrecio.views import ListaPrecio

urlpatterns = [
    path('',ListaPrecio,name="ListaPrecio"),
]