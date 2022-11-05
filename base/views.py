from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from django.contrib import messages
from django.contrib.auth import logout



def principal(request):
    titulo="Menu principal"
    context={
        'titulo':titulo
    }
    return render(request,'menu.html',context)

def error_404(request,exception):
    context={}
    return render(request,'404.html',context)


def logout_user(request):
    logout(request)
    return redirect('inicio')