from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('',views.courses,name='courses'),
    path('manage-division',views.divisions,name='divisions'),
]