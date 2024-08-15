from django.urls import path
from .views import RegisterUserView, LoginUserView, DoctorListView, DoctorDetailView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
]
