from django.urls import path
from . import views

urlpatterns = [
    path('subir-archivo/', views.subir_archivo, name='subir_archivo'),
    path('descargar-archivo/<int:archivo_id>/', views.descargar_archivo, name='descargar_archivo'),
    path('lista-archivos/', views.lista_archivos, name='lista_archivos'),
]

    
