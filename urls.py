from django.urls import path
from adminApp import views as admin_views

urlpatterns = [
    path('signin/', admin_views.signin, name='signin'),
    path('manage-student/', admin_views.manage_student, name='manage_student'),
    # Other URL patterns...
]