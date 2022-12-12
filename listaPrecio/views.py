from django.shortcuts import render


# Create your views here.

def listaPrecio (request):
    context={
        
        }
    return render(request,'listaPrecio/listaPrecio.html',context)


