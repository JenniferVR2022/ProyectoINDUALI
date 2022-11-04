from django.shortcuts import render, redirect
from componente.forms import ComponenteForm
from componente.models import Componente

# Create your views here.
def componente(request):
    titulo='Componente'
    receta=Componente.objecto.all()
    context={
        'titulo':titulo,
        'componente':componente
    }
    return render(request,'componente/componente.html',context)