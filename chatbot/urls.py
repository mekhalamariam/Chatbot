
from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='bot'),
    path('login/', views.loginpage, name='login'),
    path('signup/', views.signuppage, name='signup' ),
    path('logout/', views.logoutpage, name='logout')
]
