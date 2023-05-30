from django.urls import path
from usuarios.views import usuarios,usuarios_crear,usuarios_editar

urlpatterns = [
    
path('',usuarios,name="usuarios"),
path('usuario_crear/',usuarios_crear,name="usuarios_crear"),
path('usuario_editar/<int:pk>/',usuarios_editar,name="usuarios_editar"),

]
