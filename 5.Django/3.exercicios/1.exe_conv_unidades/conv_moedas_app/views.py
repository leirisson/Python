from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "conv_moedas/pages/index.html")


def usandoHomeTemplate(request):
    return render(request, "global/index.html") 