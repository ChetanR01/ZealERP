from django.shortcuts import render
from facultyApp.models import notification

# Create your views here.

def dashboard(request):
    return render(request, 'base.html')

def show_notifications(request):
    notifications = notification.objects.all().order_by('-created_at')
    return render(request,"studentApp/notifications.html",{'data':notifications})