from django.shortcuts import render
from receta.models import Receta
from centroCostos.models import CentroCosto

# Create your views here.

def estandarizador (request,receta=0):
    recetas= Receta.objects.filter(estado="1")
    print("###########################")
    receta_obj=Receta.objects.filter(id=receta)
    context={
        "recetas": recetas
        }
    return render(request,'estandarizador/estandarizador.html',context)


def agregar_receta(request):
    context={
        
        }
    return render(request,'estandarizador/verReceta.html',context)

def lista_centrocostos(request):
    centroCostos= CentroCosto.objects.all()
    return render(request, 'estandarizador.html', {'centroCostos': centroCostos})