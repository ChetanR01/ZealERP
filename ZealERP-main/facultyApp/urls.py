from django.urls import path, include
from . import views

app_name = 'staff'

urlpatterns = [
    # Faculty Dashboard
    path('', views.dashboard, name='dashboard'),

    # Faculty Leave Requests
    path('apply_leave/', views.apply_leave, name='apply_leave'),  # Faculty applies for leave
    path('faculty_leave_request/', views.faculty_leave_request, name='faculty_leave_request'),  # Faculty's leave requests

]