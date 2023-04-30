from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from usuarios.forms import UsuarioForm
from usuarios.models import Usuario



# Create your views here.
@login_required(login_url='inicio')
def usuarios(request):
    titulo="Usuarios"
    usuarios= Usuario.objects.all()
    context={
        'titulo':titulo,
        'usuarios':usuarios
    }
    return render(request,'usuarios/usuarios.html',context)



def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('usuarios')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'usuarios/usuario.html', context)



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










