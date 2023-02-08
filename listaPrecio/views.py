from django.shortcuts import render, redirect
from listaPrecio.models import ListaPrecio
from listaPrecio.forms import listaPForm

# Create your views here.

def listaPrecio(request):
    listaPrecio = ListaPrecio.objects.all()
    return render(request,'listaPrecio/listaPrecio.html',{'listaPrecio': listaPrecio})

def listap_crear(request):
    formulario = listaPForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('listaPrecio')
    return render(request, 'listaPrecio/listapCrear.html', {'formulario': formulario})



