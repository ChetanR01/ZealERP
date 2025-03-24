from django.shortcuts import render
from .models import notification

# Create your views here.

def dashboard(request):
    return render(request, 'facultyApp/index.html')

def show_notification(request):
    notifications = notification.objects.all().order_by('-created_at')
    for noti in notifications:
        print(noti)
    return render(request,"facultyApp/notification.html",{'data':notifications})