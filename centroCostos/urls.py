from django.urls import path
from centroCostos.views import centroCostos,centroc_crear

urlpatterns = [
    path('',centroCostos,name="centroCostos"),
    path('crear/',centroc_crear,name="centroc-crear"),
]

