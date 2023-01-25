from django.shortcuts import render, redirect
from listaPrecio.models import ListaPrecio
from listaPrecio.forms import listaPForm

# Create your views here.

def listaPrecio (request):
    context={
        
        }
    return render(request,'listaPrecio/listaPrecio.html',context)


def listap_crear(request):
    titulo="listap-crear"
    if request.method == "POST":
        form= listaPForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaPrecio')
        else:
            print("Error")
    else:
        form= listaPForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'listaPrecio/listapCrear.html',context)



