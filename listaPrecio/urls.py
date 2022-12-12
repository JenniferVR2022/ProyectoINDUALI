from django.urls import path 
from listaPrecio.views import listaPrecio

urlpatterns = [
  path('',listaPrecio,name="listaPrecio"),
]


    