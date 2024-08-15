# urls.py

from django.urls import path
from .views import register_doctor, login_doctor

urlpatterns = [
    path('register/', register_doctor, name='register_doctor'),
    path('login/', login_doctor, name='login_doctor'),
]
