from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


#home do site /
def home_page(response):
    return HttpResponse("pagina inicial da aplicação do siste")


# pagina de contatos /contatos
def contato(response):
    return HttpResponse("pagina de contatos")

# pagina de sobre /sobre
def sobre(response):
    return HttpResponse("pagina de sobre ")
