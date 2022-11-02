"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from base.views import inicio,error_404,principal

from base.views import loggedIn,logout_user
from django.contrib.auth.views import LoginView as login

####### Importes para subir imágenes #######
from django.conf import settings
from django.conf.urls.static import static
############################################

handler404= error_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login.as_view(),name='inicio'),
    path('',inicio,name='inicio'),
    path('menu/',principal,name='menu-principal'),  
    path('usuarios/',include('usuarios.urls')),
    
        
    path('centroCostos/',include('centroCostos.urls')),  
    path('componente/',include('componente.urls')),  
  
  path('loggedin/',loggedIn,name="inicio-sesion"),
    path('logout/',logout_user,name="logout"),


]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)  

