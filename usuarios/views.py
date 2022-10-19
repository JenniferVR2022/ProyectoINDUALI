from django.shortcuts import render, redirect
from usuarios.forms import UsuarioForm
from usuarios.models import Usuario


# Create your views here.
def usuarios(request):
    titulo="Usuarios"
    usuarios= Usuario.objects.all()
    context={
        'titulo':titulo,
        'usuarios':usuarios
    }
    return render(request,'usuarios/usuarios.html',context)


def usuarios_crear(request):
    if request.method =='POST':
        form=UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            print("El usuario de guardo correctamente")
            return redirect('usuarios')
        else:
             print("El usuario no se guardo ")
    else:
        form=UsuarioForm ()        
    
    context={
        "form":form
    }
    return render(request,'usuarios/usuarios-crear.html',context)

def usuarios_editar(request, pk):
    titulo="Usuarios - Editar"
    usuario= Usuario.objects.get(id=pk)
    if request.method == "POST":
        form= UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            print("Error al guardar")
    else:
        form= UsuarioForm(instance=usuario)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'usuarios/usuarios-crear.html',context)