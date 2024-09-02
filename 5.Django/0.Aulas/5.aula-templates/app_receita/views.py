from django.shortcuts import render
from django.http import httpResponse
# Create your views here.

def home_page(request):
    return httpResponse("Home page da aplicação")