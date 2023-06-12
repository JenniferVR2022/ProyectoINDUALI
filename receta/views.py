from django.shortcuts import render, redirect
from receta.models import Receta
from receta.forms import recetaForm
from ingrediente.models import Ingrediente
from .models import Receta, Ingrediente


def receta(request):
    receta = Receta.objects.all()
    return render(request,'receta/receta.html',{'receta': receta})

def receta_crear(request):
    if request.method == 'POST':
        form = recetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.save()
            return redirect('detalle_receta', pk=receta.pk)
    else:
        form = recetaForm()
    return render(request, 'receta/recetaCrear.html', {'form': form})


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


def editarR(request,id):
    receta = Receta.objects.get(id=id)
    formulario2 = recetaForm(
        request.POST or None, request.FILES or None, instance=receta)
    if formulario2.is_valid() and request.POST:
        formulario2.save()
        return redirect('receta')
    return render(request, 'receta/editarReceta.html', {'formulario2': formulario2})

def detalle_receta(request, pk):
    receta = Receta.objects.get(pk=pk)
    return render(request, 'receta/detalle_receta.html', {'receta': receta})


import csv
from django.db import transaction
from .models import Receta, Componente, Ingrediente

def importar_recetas_desde_csv(archivo_csv):
    with open(archivo_csv, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Ignorar la primera fila si contiene encabezados

        recetas = []
        for row in reader:
            cod_receta = row[0]
            nom_receta = row[1]
            estado = row[2]
            estandar = row[3]
            preparacion = row[4]

            # Obtener objetos Componente e Ingrediente relacionados
            nom_componente = row[5]
            componente = Componente.objects.get(nombre=nom_componente)

            nom_ingrediente = row[6]
            ingrediente = Ingrediente.objects.get(nombre=nom_ingrediente)

            receta = Receta(
                codReceta=cod_receta,
                nomReceta=nom_receta,
                estado=estado,
                estandar=estandar,
                preparacion=preparacion,
                nomComponente=componente,
                nomIngrediente=ingrediente,
            )
            recetas.append(receta)

    # Crear los objetos Receta en la base de datos en una transacción
    with transaction.atomic():
        Receta.objects.bulk_create(recetas)
