from django.shortcuts import render, redirect
from app_gestao_de_livros.models import Livro
# Create your views here.

def home(request):
    return render(request, "app_gestao_de_livros/pages/home_cadastro.html")

def cadastro(request):
    return render(request, "app_gestao_de_livros/pages/cadastro.html")

def listagem(request):

    livros = {
        "livros": Livro.objects.all()
    }

    return render(request, "app_gestao_de_livros/pages/listagem.html", livros)

def salvar(request):
    titulo = request.POST.get("titulo")
    autor = request.POST.get("autor")
    qtd_paginas = request.POST.get("qtd_pagina")
    data_publicacao = request.POST.get("data_publicacao")

    Livro.objects.create(titulo=titulo, autor=autor, quantidade_paginas = qtd_paginas, ano_publicacao=data_publicacao)

    return redirect('listagem')


def editar_cad(request, id):

    
    livro = Livro.objects.get(id = id)

    return render(request, "app_gestao_de_livros/pages/editar.html", {"livro":livro})
    
    

def salvar_edit(request, id):
    livro = Livro.objects.get(id =id)

    novo_titulo  = request.POST.get("titulo")
    novo_autor   = request.POST.get("autor")
    nova_paginas = request.POST.get("qtd_pagina")
    nova_data    = request.POST.get("data_publicacao")

    livro.titulo = novo_titulo
    livro.autor = novo_autor
    livro.quantidade_paginas = nova_paginas
    livro.ano_publicacao = nova_data

    livro.save()

    return redirect("listagem")


def deletar(request, id):
    
    livro = Livro.objects.get(id = id)
    livro.delete()
    
    return redirect("listagem")