from django.shortcuts import render

# Create your views here.
def pagina_incial(request):
    return render(request, "app_cadastro/pages/home.html")