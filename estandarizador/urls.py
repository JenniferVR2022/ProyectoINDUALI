from django.urls import path
from estandarizador.views import estandarizador

urlpatterns = [
    path('',estandarizador,name="estandarizador"),
]