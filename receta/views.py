from django.shortcuts import render, redirect
from receta.models import Receta
from receta.forms import recetaForm



def receta(request):
    receta = Receta.objects.all()
    return render(request,'receta/receta.html',{'receta': receta})


def receta_crear(request):
    formulario = recetaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('receta')
    return render(request, 'receta/recetaCrear.html', {'formulario': formulario})