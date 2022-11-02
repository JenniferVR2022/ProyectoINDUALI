from django.urls import path
from centroCostos.views import centroCostos

urlpatterns = [
    path('centroCostos/',centroCostos,name="centroCostos"),

]
