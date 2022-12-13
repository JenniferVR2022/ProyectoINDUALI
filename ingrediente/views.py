from django.shortcuts import render, redirect
from ingrediente.models import Ingrediente
from ingrediente.forms import IngredienteForm


# Create your views here.

def ingrediente(request):
    context={
        
        }
    return render(request,'ingrediente/ingrediente.html',context)


def ingrediente_crear(request):
    titulo="Ingrediente - Crear"
    if request.method == "POST":
        form= IngredienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingrediente')
        else:
            print("Error")
    else:
        form= IngredienteForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'ingrediente/ingredienteCrear.html',context)

