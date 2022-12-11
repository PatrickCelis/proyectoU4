from .forms import ProyectoForm
from .models import Project
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from proyecto.models import Project
from django.contrib import messages



def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def home(request):
    return render(request, 'home.html')


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/signup')  # profile
        else:
            msg = 'Nombre de usuario o contraseña incorrectos'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/')





def index(request):
    projects = Project.objects.all()

    return render(request, 'index.html', {'projects':projects})


def creacion_exitosa(request):
    return redirect ('/proyecto')

def Insertarformulario(request):
    if request.method=='POST':
        if request.POST.get('foto') and request.POST.get('title') and request.POST.get('descripcion') and request.POST.get('tags') and request.POST.get('github'):
            saverecord=Project()
            saverecord.foto=request.POST.get('foto')
            saverecord.title = request.POST.get('title')
            saverecord.descripcion = request.POST.get('descripcion')
            saverecord.tags = request.POST.get('tags')
            saverecord.github = request.POST.get('github')
            saverecord.save()
            messages.success(request,'El proyecto se guardó exitosamente')
            return render(request, "formulario.html")
    else:
        return render(request, "formulario.html")


def Insertarproyecto(request):
    context = {}
    context['form'] = ProyectoForm()

    if request.method == "POST":
        form = ProyectoForm(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            form.save()
            return redirect('proyecto')
    else:
        form = ProyectoForm()

    context = {'forms': form}

    return render(request, "form.html", context)














