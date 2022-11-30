from django.shortcuts import render, redirect
from receta.models import Receta
from receta.forms import RecetaForm,RecetaDetalle
from django.contrib import messages
from usuarios.models import Usuario

# Create your views here.
def receta(request, modal_status='hid'):
    titulo="Receta"
    receta= Receta.objects.filter(estado='1')

    ### cuerpo del modal ###
    modal_title= ""
    modal_txt= ""
    modal_submit= ""
    ########################

    pk_receta = ""
    tipo =None
    form_update= None
    form =RecetaForm()

    if request.method == "POST" and 'form-crear' in request.POST:
        form= RecetaForm(request.POST)
        if form.is_valid():
            super = form.save(commit=False)
            super=Usuario.objects.get(user_id=request.user.id)
            super.save()
            messages.success(
                request,f"La Receta {super.codReceta} ha sido abierta!"
            )
            if super.estado == 'Activo':
                return redirect('f-d-activo', super.codReceta)
            else:
                return redirect('f-d-inactivo', super.codReceta)

            return redirect('receta')
        else:
            form= RecetaForm(request.POST)
            messages.error(
                request,"Error al abrir la receta"       
            )
      

    if request.method == "POST" and 'form-editar' in request.POST:
        modal_status= 'show'
        pk_receta = request.POST['pk']
        receta= receta.objects.get(id=pk_receta)

        ## cuerpo del modal ##
        modal_title = f"Editar {receta}"
        modal_submit="Editar"
        #######################

        tipo="editar"
        form_update= recetaUpdateForm(instance=receta)
        
        
        
        if request.POST['tipo'] == 'editar':
            pk_receta = request.POST['modal-pk']
            receta = receta.objects.get(id=pk_receta)
            form_update=recetaUpdateForm(request.POST, instance=receta)

            if form_update.is_valid():
                form_update.save()
                messages.success(
                    request,f"Se editó la receta {Receta.nomReceta} exitosamente!"
                )
                return redirect('receta')
        
    context={
        'titulo':titulo,
        'receta':receta,
        'form':form,
        'modal_status':modal_status,
        'modal_submit': modal_submit,
        'modal_title': modal_submit,
        'modal_txt': modal_txt,
        'pk': pk_receta,
        'tipo': tipo,
        'form_update':form_update

    }
    return render(request,'receta/receta.html',context)