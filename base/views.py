from django.shortcuts import render, redirect
from django.views.defaults import page_not_found


def inicio(request):
    context={}
    return render(request,'ingreso.html',context)

def error_404(request,exception):
    context={}
    return render(request,'404.html',context)