from django.urls import path
from app_vendas import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("pessoas_cadastradas/", views.todos_clientes, name="pessoas"),
    path("cadastro/", views.cadastro_cliente, name="cadastro_cliente"),

]
