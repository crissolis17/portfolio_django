from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import Contactoform
from.models import Proyecto, Contacto

# Create your views here.
def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos': proyectos})

def pokeApi (request):
    return render (request, 'PokeApi.html')

#VISTAS CRUD ADMINISTRACION DE USUARIOS EN EL FORMULARIO DE CONTACTO

def contacto_nuevo(request):
    # Si la solicitud es de tipo POST, se procesa el formulario
    if request.method == "POST":
        # Se crea una instancia del formulario con los datos enviados
        form = Contactoform(request.POST)
        # Si el formulario es válido, se guarda el nuevo contacto
        if form.is_valid():
            form.save()
            # Redirige a una página de confirmación
            return redirect('contacto_confirmacion')
    else:
        # Si la solicitud no es POST, se crea un formulario vacío
        form = Contactoform()
    # Renderiza la plantilla 'contacto_formulario.html' pasando el formulario como contexto
    return render(request, 'myportfolio/contacto_formulario.html', {'form': form})
@login_required
def contacto_detalle(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'myportfolio/contacto_detalle.html', {'contacto': contacto})

@login_required
def contacto_editar(request, pk):
    contacto =get_object_or_404(Contacto, pk=pk)
    if request.method =="POST":
        form = Contactoform(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('contacto_detalle', pk=contacto.pk)
    else:
        form = Contactoform(instance=contacto)
    return render(request, 'myportfolio/contacto_editar.html', {'form': form})

@login_required
def contacto_eliminar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    return redirect('contacto_lista')



@login_required
def contacto_lista(request):
    contactos = Contacto.objects.all()
    return render(request, 'myportfolio/contacto_lista.html', {'contactos':contactos})
def contacto_confirmacion(request):
    return render(request, 'myportfolio/contacto_confirmacion.html')

@login_required
def vista_protegida(request):
    return render(request, 'vista_protegida.html')

def proyecto_detalle(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, 'proyecto_detalle.html', {'proyecto': proyecto})