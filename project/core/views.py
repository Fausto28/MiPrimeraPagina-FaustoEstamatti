from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.views import LoginView
from .forms import *
def index(request):
    contexto={'index': False, 'about':False, 'clientes':False, 'productos':False}
    if request.path == reverse('core:index'):
        contexto['index']= True
    elif request.path == reverse('core:about'):
        contexto['about']= True
        
    elif request.path == reverse('core:clientes'):
        contexto['clientes']= True
        
    elif request.path == reverse('core:productos'):
        contexto['productos']= True
        
    return render(request, "core/index.html",contexto)

def about(request):
    
    return render(request, "core/about.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"
    
def register(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/index.html')
    else:
        form= CustomUserCreationForm()
            
    return render(request, "core/register.html", {"form": form})