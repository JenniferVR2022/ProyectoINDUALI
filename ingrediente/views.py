from django.shortcuts import render, redirect
from ingrediente.models import Ingrediente
from ingrediente.forms import IngredienteForm
from django.contrib import messages
from receta.forms import RecetaForm

def ingrediente(request, modal_status='hid'):
    titulo="Ingrediente"
    ingrediente= Ingrediente.objects.filter(estado='1')
    
    ### cuerpo del modal ###
    modal_title= ""
    modal_txt= ""
    modal_submit= ""
    ########################

    pk_ingrediente = ""
    tipo =None
    form_update= None
    form =IngredienteForm()
    
 