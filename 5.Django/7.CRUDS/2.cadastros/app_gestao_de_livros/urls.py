from django.urls import path
from app_gestao_de_livros import views
from app_gestao_de_livros import autenticacao 


urlpatterns = [
    path("", views.home, name="home"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("salvar/", views.salvar, name="salvar"),
    path("listagem/", views.listagem, name="listagem"),
    path("editar/<int:id>", views.editar_cad, name="editar_cad"),
    path("salvar_edit/<int:id>", views.salvar_edit, name="salvar_edit"),
    path("deletar/<int:id>", views.deletar, name="deletar"),
    path('entrar/', autenticacao.entrar, name="entrar"),
    path("sair/", autenticacao.sair, name="sair"),
    
]
