from django.shortcuts import render, redirect
from ingrediente.models import Ingrediente
from ingrediente.forms import IngredienteForm
from django.contrib.auth.decorators import login_required


@login_required
def ingrediente(request):
    ingrediente = Ingrediente.objects.all()
    return render(request, 'ingrediente/ingrediente.html', {'ingrediente': ingrediente})

@login_required
def ingrediente_crear(request):
    formulario = IngredienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('ingrediente')
    return render(request, 'ingrediente/ingredienteCrear.html', {'formulario': formulario})

@login_required
def eliminar(request,id):
    ingrediente = Ingrediente.objects.get(id=id)
    ingrediente.estado = False
    ingrediente.save()
    return redirect('ingrediente')

@login_required
def editar(request,id):
    ingrediente = Ingrediente.objects.get(id=id)
    formulario = IngredienteForm(
        request.POST or None, request.FILES or None, instance=ingrediente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('ingrediente')
    return render(request, 'ingrediente/editarIngrediente.html', {'formulario': formulario})






# def logout_request(request):
    logout(request)
    messages.info(request, "Saliste Exitosamente")
# return redirect("main:homepage")
# def ingrediente_crear(request):
#     titulo="Ingrediente - Crear"
#     if request.method == "POST":
#         form= IngredienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('ingrediente')
#         else:
#             print("Error")
#     else:
#         form= IngredienteForm()
#     context={
#         'titulo':titulo,
#         'form':form
#     }
#     return render(request,'ingrediente/ingredienteCrear.html',context)

# def ingredientes(request):
#     ingredientes = Ingrediente.objects.all()
#     return render(request,'ingrediente/ingrediente.html',{'ingredientes' : ingredientes})
