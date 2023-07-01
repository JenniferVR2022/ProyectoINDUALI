from django.shortcuts import render, redirect,get_object_or_404
from receta.forms import recetaForm
from ingrediente.models import Ingrediente
from .models import Receta, Ingrediente
from .forms import recetaForm
from django.contrib.auth.decorators import login_required


@login_required
def receta(request):
    receta = Receta.objects.all()
    return render(request,'receta/receta.html',{'receta': receta})

@login_required
def receta_crear(request):
    if request.method == 'POST':
        form = recetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.save()
            return redirect('detalle_receta', pk=receta.pk)
    else:
        form = recetaForm()
    return render(request, 'receta/recetaCrear.html', {'form': form})


@login_required
def receta_agregar(request):
    Ingredientes = Ingrediente.objects.values_list('nomIngrediente', flat=True)
    context = {
        'ingrediente': Ingredientes,   
    }
    return render(request, 'receta/recetaAgregar.html', context)

def eliminar(request,id):
    receta = Receta.objects.get(id=id)
    receta.estado = False
    receta.save()
    return redirect('receta')


@login_required
def editarR(request, pk):
    receta = get_object_or_404(Receta, id=pk)
    if request.method == 'POST':
        form = recetaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('detalle_receta', receta_id=pk)  # Cambio aquí
               
    else:
        form = recetaForm(instance=receta)
    return render(request, 'receta/editarReceta.html', {'form': form, 'receta': receta})


@login_required
def detalle_receta(request, pk):
    receta = Receta.objects.get(id=pk)
    return render(request, 'receta/detalle_receta.html', {'receta': receta})
