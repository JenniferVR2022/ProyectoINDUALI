from django.urls import path
from centroCostos.views import centroCostos,centroc_crear,editar

urlpatterns = [
    path('',centroCostos,name="centroCostos"),
    path('crear/',centroc_crear,name="centroc-crear"),
    path('editar/<int:id>', editar, name="editar-CC"),
]

