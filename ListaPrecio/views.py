from django.shortcuts import render

# Create your views here.
def ListaPrecio(request):
    context={

    }
    return render(request, 'ListaPrecio/listaPrecio.html', context)
