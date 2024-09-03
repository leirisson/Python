from django.urls import path
from citacoes_app.views import pagina_incial


urlpatterns = [
    path("", pagina_incial)
]
