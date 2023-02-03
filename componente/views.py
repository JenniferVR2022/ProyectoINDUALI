from django.shortcuts import render, redirect
from componente.models import Componente
from componente.forms import componenteForm

# Create your views here.
def componente(request):
    titulo='Componente'
    componente=Componente.objects.all()
    context={
        'titulo':titulo,
        'componente':componente
    }
    return render(request,'componente/componente.html',context)




def crear_componente(request):
    titulo="crear-componente"
    if request.method == "POST":
        form= componenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Componente')
        else:
            print("Error")
    else:
        form= componenteForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'componente/crearComponente.html',context)
