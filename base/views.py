from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from usuarios.models import Usuario


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenido {user.nombres} {user.apellidos}")
            return redirect("home")
        else:
            messages.error(request, "Correo electrónico o contraseña incorrecta")
            return redirect("login")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('login')



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

