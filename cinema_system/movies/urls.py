from django.urls import path
from . import views

urlpatterns = [
    path('<str:title>', views.moviePage, name='moviePage'),

]