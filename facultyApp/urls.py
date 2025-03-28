from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('notified/', views.show_fac_notification, name='notified'),
    path('manage_leave/', views.manage_leave, name='manage_leave'),
    path('approve_leave/<int:leave_id>/', views.approve_leave, name='approve_leave'),
    path('reject_leave/<int:leave_id>/', views.reject_leave, name='reject_leave'),

]