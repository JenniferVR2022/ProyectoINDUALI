from django.shortcuts import render, redirect
from centroCostos.models import CentroCosto
from centroCostos.forms import CentroCostoForm


# Create your views here.
def centroCostos(request):
    centroCostos= CentroCosto.objects.all()
    return render(request,'centroCostos/centroCostos.html',{'centroCostos': centroCostos})


def centroc_crear(request):
    formulario = CentroCostoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('centroCostos')
    return render(request, 'centroCostos/crearCentroc.html', {'formulario': formulario})




