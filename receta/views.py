from django.shortcuts import render, redirect
from receta.models import Receta
from receta.forms import RecetaForm

# Create your views here.
def receta(request):
    titulo='Receta'
    receta=Receta.objects.all()
    form=RecetaForm()
    context={
        'form':form,
        'titulo':titulo,
        'receta':receta
    }
    return render(request,'receta/receta.html',context)



 if request.method == "POST" and 'form-editar' in request.POST:
        modal_status= 'show'
        pk_ingrediente = request.POST['pk']
        Ingrediente= Ingrediente.objects.get(id=pk_ingrediente)

        ## cuerpo del modal ##
        modal_title = f"Editar {ingrediente}"
        modal_submit="Editar"
        #######################

        tipo="editar"
        form_update= IngredienteUpdateForm(instance=ingrediente)