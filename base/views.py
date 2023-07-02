from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from django.contrib import messages
from django.contrib.auth import logout
from usuarios.models import Usuario
from django.contrib.auth.decorators import login_required


@login_required
def principal(request):
    titulo="Menu principal"
    context={
        'titulo':titulo
    }
    return render(request,'menu.html',context)


def inicioAdmin(request):
    titulo="Tablero Principal"
    cantidad_usuarios= Usuario.objects.all().count()
    
    labels_stock=[]
    data_stock=[]
   

    context={
        'titulo':titulo,
        'cantidad_usuarios':cantidad_usuarios,
        'labels_stock': labels_stock,
        'data_stock':data_stock,
    }
    return render(request,'index-admin.html', context)


def error_404(request,exception):
    context={}
    return render(request,'404.html',context)


def logout_user(request):
    logout(request)
    return redirect('inicio')


