from django.shortcuts import render, redirect
from receta.models import Receta
from receta.forms import RecetaForm,RecetaDetalle
from django.contrib import messages
from usuarios.models import Usuario

def receta(request):
    context={
        
        }
    return render(request,'receta/receta.html',context)


def receta_crear(request):
    titulo="Receta - Crear"
    if request.method == "POST":
        form= RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receta')
        else:
            print("Error")
    else:
        form= RecetaForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'receta/recetaCrear.html',context)