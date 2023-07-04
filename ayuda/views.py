from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Archivo

def subir_archivo(request):
    if request.method == 'POST':
        archivo = request.FILES['archivo']
        nuevo_archivo = Archivo(archivo=archivo)
        nuevo_archivo.save()
        return redirect('lista_archivos')
    return render(request, 'ayuda/subir_archivo.html')

def descargar_archivo(request, archivo_id):
    archivo = Archivo.objects.get(id=archivo_id)
    response = HttpResponse(archivo.archivo, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % archivo.archivo.name
    return response

def lista_archivos(request):
    archivos = Archivo.objects.all()
    return render(request, 'ayuda/lista_archivos.html', {'archivos': archivos})
