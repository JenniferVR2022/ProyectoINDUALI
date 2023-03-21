from django.shortcuts import render, redirect
from receta.models import Receta,Ingrediente
from receta.forms import RecetaForm,recetaForm



def receta(request):
    receta = Receta.objects.all()
    return render(request,'receta/receta.html',{'receta': receta})


#def receta_crear(request):
    #formulario = recetaForm(request.POST or None, request.FILES or None)
    #if formulario.is_valid():
     #   formulario.save()
     #   return redirect('receta')
    #return render(request, 'receta/recetaCrear.html', {'formulario': formulario})


from django.views.decorators.http import require_POST

@require_POST
def guardar_receta(request):
    # Aquí se puede procesar la solicitud POST y guardar los datos en la base de datos
    return render(request, 'receta/receta_guardada.html')


def mi_vista(request):
    form = RecetaForm()
    return render(request, 'receta/recetaCrear.html', {'form': form})


def receta_crear(request):
    ingredientes = Ingrediente.objects.values_list('nomIngrediente', flat=True)

    context = {
                'ingredientes': ingredientes,
    }

    return render(request, 'receta/recetaCrear.html', context)




