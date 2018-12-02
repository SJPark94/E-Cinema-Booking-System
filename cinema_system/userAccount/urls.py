from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.registerRequest, name='registerRequest'),
    path('activation/', views.activateAccount, name='activate'),
    path('viewProfile/', views.viewProfile, name='viewProfile'),
    path('editProfile/', views.editProfile, name='editProfile'),
    path('password/', views.changePassword, name='changePassword'),

]
