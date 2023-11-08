from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resultado.html', views.guess_request, name='guess_request'),
]