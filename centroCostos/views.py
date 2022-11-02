from django.shortcuts import render, redirect
from centroCostos.models import CentroCosto
from centroCostos.forms import CentroCostoForm


# Create your views here.
def centroCostos(request):
    titulo='CentroCosto'
    centroCostos=CentroCosto.objecto.all()
    context={
        'titulo':titulo,
        'centroCostos':centroCostos
    }
    return render(request,'centroCostos/centroCostos.html',context)

def centroCostos_crear(request):
    titulo="CentroCosto - Crear"
    if request.method == "POST":
        form= CentroCostoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('centroCostos')
        else:
            print("Error")
    else:
        form= CentroCostoForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'partials/crear.html',context)