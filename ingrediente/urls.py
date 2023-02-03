from django.urls import path 
from ingrediente.views import ingrediente,ingrediente_crear,eliminar,editar

urlpatterns = [
  path('',ingrediente,name="ingrediente"), 
  path('crear/',ingrediente_crear,name="ingrediente-crear"),
  path('eliminar/<int:id>',eliminar, name="eliminar"),  
  path('editar/<int:id>',editar, name="editar"),  
  ]

