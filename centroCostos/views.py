from django.shortcuts import render, redirect
from centroCostos.models import CentroCosto
from centroCostos.forms import CentroCostoForm
from django.contrib.auth.decorators import login_required


@login_required

def centroCostos(request):
    centroCostos= CentroCosto.objects.all()
    return render(request,'centroCostos/centroCostos.html',{'centroCostos': centroCostos})


def centroc_crear(request):
    formulario = CentroCostoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('centroCostos')
    return render(request, 'centroCostos/crearCentroc.html', {'formulario': formulario})



def editar(request,id):
    centroCostos = CentroCosto.objects.get(id=id)
    formulario = CentroCostoForm(
        request.POST or None, request.FILES or None, instance=centroCostos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('centroCostos')
    return render(request, 'centroCostos/editarCentroC.html', {'formulario': formulario})



