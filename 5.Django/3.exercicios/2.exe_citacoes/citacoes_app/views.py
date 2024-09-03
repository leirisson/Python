from django.shortcuts import render

# Create your views here.
def pagina_incial(request):
    return render(request, "citacoes/pages/index.html")