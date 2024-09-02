from django.urls import path
from receitas_app.views import home_page, sobre, contato

urlpatterns = [
     path('', home_page),
     path('sobre/', sobre),
     path('contatos/', contato)
]

