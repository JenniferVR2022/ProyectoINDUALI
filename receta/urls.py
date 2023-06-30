from django.urls import path
from receta.views import receta,receta_crear,receta_agregar,editarR,eliminar,detalle_receta
from . import views
urlpatterns = [
    path('',receta,name="receta"),
    path('crear/',receta_crear,name="crear-receta"),
    path('agregar/',receta_agregar,name="receta-agregar"),
    path('eliminar/<int:id>', eliminar, name="eliminar"),
    path('editarR/<int:pk>', editarR, name="editarR"),
    path('detalle-receta/<int:pk>/', detalle_receta, name='detalle_receta'),
    path('detalle-receta/<int:receta_id>/', views.detalle_receta, name='detalle_receta'),
    

]










    

