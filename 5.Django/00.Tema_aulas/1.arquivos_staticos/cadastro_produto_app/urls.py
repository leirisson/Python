from django.urls import path
from cadastro_produto_app.views import home_page, cadastro_usuario
urlpatterns = [
    path("", home_page, name="home"),
    path("cadastro/", cadastro_usuario, name="cadastro")
]
