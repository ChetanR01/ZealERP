from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('notificate/', views.show_notifications, name='notificate'),

    path('view_subjects', views.view_subjects, name = 'view_subjects'),

    path('',views.courses,name='courses'),
    path('',views.divisions,name='divisions'),

]