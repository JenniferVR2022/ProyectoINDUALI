from django.shortcuts import render, redirect
from receta.models import Receta
from receta.forms import recetaForm
from ingrediente.models import Ingrediente
from .models import Receta, Ingrediente


def receta(request):
    receta = Receta.objects.all()
    return render(request,'receta/receta.html',{'receta': receta})

def receta_crear(request):
    formulario = recetaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('receta')
    return render(request, 'receta/recetaCrear.html', {'formulario': formulario})

def receta_agregar(request):
    Ingredientes = Ingrediente.objects.values_list('nomIngrediente', flat=True)
    context = {
        'ingrediente': Ingredientes,   
    }
    return render(request, 'receta/recetaAgregar.html', context)

def eliminar(request,id):
    receta = Receta.objects.get(id=id)
    receta.estado = False
    receta.save()
    return redirect('receta')


def editarR(request,id):
    receta = Receta.objects.get(id=id)
    formulario2 = recetaForm(
        request.POST or None, request.FILES or None, instance=receta)
    if formulario2.is_valid() and request.POST:
        formulario2.save()
        return redirect('receta')
    return render(request, 'receta/editarReceta.html', {'formulario2': formulario2})




def detalle_receta(request, receta_id):
    receta = Receta.objects.get(id=receta_id)
    ingredientes = Ingrediente.objects.filter(receta=receta)
    return render(request, 'detalle_receta.html', {'receta': receta, 'ingredientes': ingredientes})