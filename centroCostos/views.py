from django.shortcuts import render, redirect
from centroCostos.models import CentroCosto
from centroCostos.forms import CentroCostoForm


# Create your views here.
def centroCostos(request):
    titulo='CentroCosto'
    centroCostos=CentroCosto.objects.all()
    context={
        'titulo':titulo,
        'centroCostos':centroCostos
    }
    return render(request,'centroCostos/centroCostos.html',context)



