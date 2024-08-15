# urls.py

from django.urls import path
from .views import register_doctor, login_doctor, MedicationListView

urlpatterns = [
    path('register/', register_doctor, name='register_doctor'),
    path('login/', login_doctor, name='login_doctor'),
    path('medications/', MedicationListView.as_view(), name='medication-list'),
    path('register/', register_doctor, name='register_doctor'),
]
