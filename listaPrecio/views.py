from django.shortcuts import render, redirect
from listaPrecio.models import ListaPrecio
from listaPrecio.forms import listaPForm
from django.contrib.auth.decorators import login_required


@login_required
def listaPrecio(request):
    listaPrecio = ListaPrecio.objects.all()
    return render(request,'listaPrecio/listaPrecio.html',{'listaPrecio': listaPrecio})

@login_required
def listap_crear(request):
    formulario = listaPForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('listaPrecio')
    return render(request, 'listaPrecio/listapCrear.html', {'formulario': formulario})

@login_required
def editar(request,id):
    listaPrecio = ListaPrecio.objects.get(id=id)
    formulario = listaPForm(
        request.POST or None, request.FILES or None, instance=listaPrecio)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('listaPrecio')
    return render(request, 'listaPrecio/editarListaprecio.html', {'formulario': formulario})

