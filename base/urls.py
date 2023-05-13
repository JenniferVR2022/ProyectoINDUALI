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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import login,logout_then_login
from django.contrib.auth import login,logout
from base.views import logout_user
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from base.views import error_404, principal


handler404 = error_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.loginViem.as_view('template_name':'base/ingreso.html'. name ='login')),
    path('logout/', logout_user, name="logout"),
    # path('logout/', views.logout_request, name="logout"),
    path('principal/', principal, name='principal'),
    path('usuarios/', include('usuarios.urls')),
    path('centroCostos/', include('centroCostos.urls')),
    path('componente/', include('componente.urls')),
    path('recetas/', include('receta.urls')),
    path('ingrediente/', include('ingrediente.urls')),
    path('estandarizador/', include('estandarizador.urls')),
    path('listaPrecio/', include('listaPrecio.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
