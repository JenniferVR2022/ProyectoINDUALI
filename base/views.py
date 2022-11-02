from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from django.contrib import messages
from django.contrib.auth import logout


def inicio(request):
    context={}
    return render(request,'ingreso.html',context)

def principal(request):
    titulo="Menu Principal"
    context={
        'titulo':titulo
    }
    return render(request,'menu.html',context)

def error_404(request,exception):
    context={}
    return render(request,'404.html',context)

def loggedIn(request):
    if request.user.is_authenticated:
        respuesta:"Ingresado como "+ request.user.username
    else:
        respuesta:"No estas autenticado."
    return HttpResponse(respuesta)

def logout_user(request):
    logout(request)
    return redirect('inicio')