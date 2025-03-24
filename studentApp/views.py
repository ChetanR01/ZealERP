from django.shortcuts import render
from facultyApp.models import notification
from studentApp.models import Course



def dashboard(request):
    return render(request, 'base.html')

def show_notifications(request):
    notifications = notification.objects.all().order_by('-created_at')
    return render(request,"studentApp/notifications.html",{'data':notifications})
