from django.shortcuts import render
from .models import Course,Student

def dashboard(request):
    return render(request, 'student/index.html')

def profile(request):
    try:
        student = Student.objects.get(user=request.user)
        return render(request, 'student/profile.html', {'student': student})
    except Student.DoesNotExist:
        # If student record doesn't exist, redirect to create profile or show error
        return render(request, 'student/profile.html', {'student': None})