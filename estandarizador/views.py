from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def estandarizador(request):
    context={
        
    }
    return render(request,'estandarizador/estandarizador.html',context)