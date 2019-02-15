from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cliente

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,"Usuário e senha invalidos. Favor tentar novamente.")
    return redirect('/login/##')


def registros(request):
    return render(request, 'register.html')

def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def list_all_reg(request):
    cliente = Cliente.objects.filter

    return render(request, 'list.html', {'cliente':cliente})


