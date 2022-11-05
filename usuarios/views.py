from django.shortcuts import render, redirect
from usuarios.forms import UsuarioForm
from usuarios.models import Usuario

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='principal')
def usuarios(request):
    titulo="Usuarios"
    usuarios= Usuario.objects.all()
    context={
        'titulo':titulo,
        'usuarios':usuarios
    }
    return render(request,'usuarios/usuarios.html',context)


def usuarios_crear(request):
    titulo="Usuarios - Crear"
    if request.method =='POST':
        form=UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            print("El usuario se guardo correctamente")
            return redirect('usuarios')
        else:
             print("El usuario no se almaceno ")
    else:
        form=UsuarioForm ()        
    
    context={
        "form":form
    }
    return render(request,'usuarios/usuarios-crear.html',context)



def usuarios_editar(request, pk):
    titulo="Usuarios - Editar"
    usuario=Usuario.objects.get(id=pk)
    if request.method =='POST':
        form=UsuarioForm(request.POST, intance=usuario)
        if form.is_valid():
            form.save()
            
            return redirect('usuarios')
        else:
             print("Error al guardar los cambios")
    else:
        form=UsuarioForm(instance=usuario)       
    
    context={
        'titulo':titulo,
        "form":form
    }
    return render(request,'usuarios/usuarios-editar.html',context)











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
    return render(request,'partials/crear.html',context)

