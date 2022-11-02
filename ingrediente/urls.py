from django.urls import path 
from ingrediente.views import ingrediente

urlpatterns = [
  path('',ingrediente,name="ingrediente"),
]



