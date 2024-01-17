from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse

def index(request):
    contexto={'index': False, 'about':False, 'clientes':False}
    if request.path == reverse('core:index'):
        contexto['index']= True
    elif request.path == reverse('core:about'):
        contexto['about']= True
        
    elif request.path == reverse('core:clientes'):
        contexto['clientes']= True
        
    return render(request, "core/index.html",contexto)

def about(request):
    
    return render(request, "core/about.html")