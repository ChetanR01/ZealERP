from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('apply_leave/', views.apply_leave, name='apply_leave'),
    path('leave_requests/', views.leave_requests, name='leave_requests'),
]