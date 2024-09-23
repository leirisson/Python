from django.urls import path
from app_5w2h import views

urlpatterns = [
    path("", views.home, name="home")
]
