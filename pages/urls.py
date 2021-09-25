from django.contrib.auth import login
from django.urls import path
from .views import index,register

urlpatterns = [
    path('', index, name='home'),
    path('accounts/register/', register, name='register'),
    path('login/', login, name='login'),
]
