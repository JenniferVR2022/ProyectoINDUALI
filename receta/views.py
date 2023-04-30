from django.shortcuts import render, redirect
from receta.models import Receta
from receta.forms import recetaForm
from ingrediente.models import Ingrediente



def receta(request):
    receta = Receta.objects.all()
    return render(request,'receta/receta.html',{'receta': receta})


def receta_crear(request):
    formulario = recetaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('receta')
    return render(request, 'receta/recetaCrear.html', {'formulario': formulario})
from django.views.decorators.http import require_POST


def receta_agregar(request):
    Ingredientes = Ingrediente.objects.values_list('nomIngrediente', flat=True)
    context = {
        'ingrediente': Ingredientes,   
    }
    return render(request, 'receta/recetaAgregar.html', context)

