from django.shortcuts import render,redirect
from authAppExample.models import Account
<<<<<<< HEAD
from authAppExample.forms import InmuebleForm, CustomCreationForm
=======
from authAppExample.forms import InmuebleForm, UserRegisterForm
>>>>>>> origin/main
from django.contrib import messages

def inicio(request):
    inmuebles = Account.objects.all()
    contexto ={
        'inmuebles':inmuebles
    }
    return render(request,'index.html',contexto)


def crearInmueble(request):
    if request.method == 'GET':
        form = InmuebleForm()
        contexto = {
            'form':form
        }
    else:
        form = InmuebleForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('perfil')
    return render(request,'crear_inmueble.html',contexto)

def editarInmueble(request,id):
    inmueble = Account.objects.get(id = id)
    if request.method == 'GET':
        form = InmuebleForm(instance = inmueble)
        contexto = {
            'form':form
        }
    else:
        form = InmuebleForm(request.POST,instance=inmueble)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('perfil')
    return render(request,'crear_inmueble.html',contexto)

def eliminarInmueble(request,id):
    inmueble = Account.objects.get(id =id)
    inmueble.delete()
    return redirect('perfil')

def perfil(request):
    inmuebles = Account.objects.all()
    contexto ={
        'inmuebles':inmuebles
    }
    return render(request,'perfil.html',contexto)


def register(request):
<<<<<<< HEAD
       
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():      
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario{username}creado')
            return redirect('index')
    else: 
        form = CustomCreationForm() 
    context = {'form':form}


    return render(request,'registration/registro.html',context)
=======
    if request.method == 'POST':
	    form = UserRegisterForm(request.POST)
	    if form.is_valid():
		    form.save()
		    username = form.cleaned_data['username']
		    messages.success(request, f'Usuario {username} creado')
		    return redirect('index')
    else:
		    form = UserRegisterForm()

    context = { 'form' : form }
    return render(request, 'registration/registro.html', context)
>>>>>>> origin/main
