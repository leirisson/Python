from django.shortcuts import render
from app_vendas.models import Cadastro_cliente
# Create your views here.


def home_page(request):
    return render(request, "app_vendas/pages/home.html")

def todos_clientes(request):
    clientes  = Cadastro_cliente.objects.all()
    return render(request, "app_vendas/pages/clientes_cadastradas.html", {"clientes":clientes})

def cadastro_cliente(request):
    nome = request.POST.get("nome")
    sobre_nome = request.POST.get("sobre_nome")
    cpf = request.POST.get("cpf")
    email = request.POST.get("email")

    Cadastro_cliente.objects.create(nome=nome, sobre_nome=sobre_nome, cpf=cpf, email=email)

    clientes = Cadastro_cliente.objects.all()

    return render(request, "app_vendas/pages/cadastro_clientes.html", {"clientes":clientes})