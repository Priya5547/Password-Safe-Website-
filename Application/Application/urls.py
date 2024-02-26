from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home),
    path('Home',views.Home),
    path('signing',views.signing),
    path('Login',views.Login),
    path('SignSucces',views.process_signing_data),
    path('LoginSucces',views.login_data),
    path('Add_password',views.add_password),
    path('PasswordStorage',views.Password)
]