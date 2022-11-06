from django.shortcuts import render


# Create your views here.

def ingrediente(request):
    context={
        
        }
    return render(request,'ingrediente/ingrediente.html',context)

