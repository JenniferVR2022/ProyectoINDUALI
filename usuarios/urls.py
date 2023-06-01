from django.urls import path
from usuarios.views import usuarios,usuarios_crear,usuarios_editar

urlpatterns = [
    
path('',usuarios,name="usuarios"),
path('usuario_crear/',usuarios_crear,name="usuarios_crear"),
path('usuario-editar/<int:pk>/',usuarios_editar,name="usuarios-editar"),

]
