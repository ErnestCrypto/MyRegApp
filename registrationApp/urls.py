# Creating our views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'registrationApp'


urlpatterns = [
    path('register/', views.registerPage, name='registerPage'),
    path('', views.homePage, name='home'),
    path('login/', views.loginPage, name='loginPage'),

]
