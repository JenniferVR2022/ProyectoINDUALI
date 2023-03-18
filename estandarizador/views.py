from django.shortcuts import render
from estandarizador.models import Estandarizador
from listaPrecio.models import ListaPrecio
from centroCostos.models import CentroCosto
from receta.models import Receta

def estandarizador(request):
    lista_precios = ListaPrecio.objects.values_list('nomListaPrecio', flat=True)
    centro_costos = CentroCosto.objects.values_list('nomCentroCostos', flat=True)
    recetas = Receta.objects.values_list('nomReceta', flat=True)

    context = {
        'lista_precios': lista_precios,
        'centro_costos': centro_costos,
        'recetas': recetas,
    }

    return render(request, 'estandarizador/estandarizador.html', context)



def agregar_receta(request):
    context={
        
        }
    return render(request,'estandarizador/verReceta.html',context)
