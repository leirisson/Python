from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def entrar(request):
    if request.user.is_authenticated:
        # Se o usuário já está autenticado, redirecionar para a página principal (ou outra página)
        return redirect('home')
     
    if request == "POST":
        nome = request.POST.get("usuario")
        senha = request.POST.get("senha")

        usuario =  authenticate(request, username=nome, password=senha)

        if usuario is not None:

            login(request, usuario)
            print("Logou !!")
            return redirect('cadastro')
        else:
            print("não deu certo")
            return render(request, "app_gestao_de_livros/pages/home.html")

    return render(request, 'app_gestao_de_livros/pages/home_cadastro.html')




def sair(request):
    logout(request)
    return redirect("entrar")