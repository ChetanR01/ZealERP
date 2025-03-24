from django.shortcuts import render
from .models import notification
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Division  # Corrected import path

# Create your views here.

def dashboard(request):
    return render(request, 'base.html')

def show_fac_notification(request):
    notifications = notification.objects.all().order_by('-created_at')
    return render(request,"facultyApp/notification.html",{'data':notifications})

def divisions(request):
    divisions = Division.objects.all()
    return render(request, 'adminApp/manage_division.html', {'divisions': divisions})
