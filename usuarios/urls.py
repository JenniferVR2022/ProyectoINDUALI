from django.urls import path
from usuarios.views import usuarios,register,usuarios_editar

urlpatterns = [
    
path('usuario/',usuarios,name="usuarios"),
path('register/',register, name="register"),
path('usuario_editar/<int:pk>/',usuarios_editar,name="usuarios_editar"),



]

