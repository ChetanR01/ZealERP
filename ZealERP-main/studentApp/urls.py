from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('apply_leave/', views.apply_leave, name='apply_leave'),
    path('leave_request/', views.leave_request, name='leave_request'),

    path('notificate/', views.show_notifications, name='notificate'),

    path('apply_leave/', views.apply_leave, name='apply_leave'),
    path('leave_request/', views.leave_request, name='leave_request'),


    path('view_subjects', views.view_subjects, name = 'view_subjects'),

    path('',views.courses,name='courses'),
    path('manage-division',views.divisions,name='divisions'),

]