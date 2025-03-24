from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('notified/', views.show_fac_notification, name='notified'),

]