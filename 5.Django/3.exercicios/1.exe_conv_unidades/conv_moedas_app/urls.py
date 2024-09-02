from django.urls import path
from conv_moedas_app.views import index, usandoHomeTemplate

urlpatterns = [
    path("", index),
    path("home_global/", usandoHomeTemplate),
]
