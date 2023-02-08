from django.shortcuts import render, redirect
from componente.models import Componente
from componente.forms import componenteForm

# Create your views here.

def componente(request):
    componente = Componente.objects.all()
    return render(request,'componente/componente.html',{'componente': componente})


def crear_componente(request):
    formulario = componenteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('componente')
    return render(request, 'componente/crearComponente.html', {'formulario': formulario})