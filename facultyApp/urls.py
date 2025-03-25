from django.urls import path
from . import views

app_name = 'faculty'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Dashboard page
    path('apply-leave/', views.apply_leave, name='apply_leave'),  # Apply for leave
    path('leave-requests/', views.leave_requests, name='leave_requests'),  # View leave requests
    path('faculty-leave-list/', views.faculty_leave_list, name='faculty_leave_list'),  # List of all faculty leaves
    path('approve-reject-leave/<int:leave_id>/', views.approve_reject_staff_leave, name='approve_reject_staff_leave'),  # Approve/Reject leave request by ID
]
