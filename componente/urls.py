
from django.urls import path
from componente.views import componente

urlpatterns = [
    path('componente/',componente,name="componente"),

]