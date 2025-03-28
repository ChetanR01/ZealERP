from django.urls import path, include
from . import views

app_name = 'staff'

urlpatterns = [
    # Faculty Dashboard
    path('', views.dashboard, name='dashboard'),

    # Faculty Leave Requests
    path('apply_leave/', views.apply_leave, name='apply_leave'),  # Faculty applies for leave
    path('faculty_leave_request/', views.faculty_leave_request, name='faculty_leave_request'),  # Faculty's leave requests
    path('notified/', views.show_fac_notification, name='notified'),
    path('manage_leave/', views.manage_leave, name='manage_leave'),
    path('approve_leave/<int:leave_id>/', views.approve_leave, name='approve_leave'),
    path('reject_leave/<int:leave_id>/', views.reject_leave, name='reject_leave'),
]