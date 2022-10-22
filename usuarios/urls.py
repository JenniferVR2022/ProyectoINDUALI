from django.urls import path
from usuarios.views import usuarios,usuarios_crear

urlpatterns = [
    
path('usuario/',usuarios,name="usuarios"),
path('crear/',usuarios_crear,name="usuarios_crear"),


]
