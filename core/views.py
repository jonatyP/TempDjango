from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cliente


def login_user(request):
    return render(request, 'login.html')

@login_required(login_url='/login/')
def set_cliente(request):
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('telefone')
    endereco = request.POST.get('endereco')
    email = request.POST.get('email')
    cliente_id =request.POST.get('cliente-id')
    # user = request.user
    if cliente_id:
        cliente = Cliente.objects.get(id=cliente_id)
        cliente.nome = nome
        cliente.cpf = cpf
        cliente.telefone = telefone
        cliente.endereco = endereco
        cliente.email = email
        cliente.save()
    else:
        cliente = Cliente.objects.create(
        nome=nome, cpf=cpf, telefone=telefone, endereco=endereco, email=email
        )
    url = '/reg/detali/{}/'.format(cliente.id)
    return redirect(url)

@login_required(login_url='/login/')
def delet_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('/')

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

@login_required(login_url='/login/')
def registros(request):
    cliente_id =request.GET.get('id')
    if cliente_id:
        cliente = Cliente.objects.get(id=cliente_id)
        return render(request, 'register.html', {'cliente':cliente})
    return render(request, 'register.html')

@login_required(login_url='/login/')
def reg_detali(request, id):
    cliente = Cliente.objects.get(id=id)
    print(cliente.id)
    return render(request, 'detalhe.html', {'cliente':cliente})

@login_required(login_url='/login/')
def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def list_all_reg(request):
    cliente = Cliente.objects.filter
    return render(request, 'list.html', {'cliente':cliente})



