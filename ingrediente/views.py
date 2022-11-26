from django.shortcuts import render, redirect
from ingrediente.models import Ingrediente
from ingrediente.forms import IngredienteForm

def ingrediente(request):
    titulo='Ingrediente'
    ingrediente=Ingrediente.objects.all()
    form=IngredienteForm()
    context={
        'form':form,
        'titulo':titulo,
        'ingrediente':ingrediente
    }
    return render(request,'ingrediente/ingrediente.html',context)