from django.shortcuts import render


# Create your views here.

def estandarizador (request):
    context={
        
        }
    return render(request,'estandarizador/estandarizador.html',context)


def agregar_receta(request):
    context={
        
        }
    return render(request,'estandarizador/verReceta.html',context)