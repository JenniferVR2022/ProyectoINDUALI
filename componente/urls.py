
from django.urls import path
from componente.views import componente,crear_componente,editar_componente,eliminar_componente

urlpatterns = [
    path('componente/',componente,name="componente"),
    path('crear/',crear_componente,name="crear-componente"),
    path('editar/<int:id>',editar_componente, name="editar-componente"),
    path('eliminar/<int:id>',eliminar_componente, name="eliminar-componente"),
]