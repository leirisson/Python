from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, "cadastro_produtos/pages/base.html")


def cadastro_usuario(request):
    return render(request, "cadastro_produtos/pages/formulario.html")