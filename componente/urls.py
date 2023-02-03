
from django.urls import path
from componente.views import componente,crear_componente

urlpatterns = [
    path('componente/',componente,name="componente"),
    path('crear/',crear_componente,name="crear-componente"),
]