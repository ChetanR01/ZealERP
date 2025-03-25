from django.shortcuts import render, redirect
from facultyApp.models import notification
from studentApp.models import Course
from studentApp.models import Student, Division 
from adminApp.models import Subject




def dashboard(request):
    return render(request, 'base.html')

def show_notifications(request):
    notifications = notification.objects.all().order_by('-created_at')
    return render(request,"studentApp/notifications.html",{'data':notifications})
def view_subjects(request):
    if request.user.is_authenticated:
        try:
            # Attempt to get the user's existing cart
            student = Student.objects.get(user=request.user)
         
            course = student.course
            if course : 
                subjects = Subject.objects.filter(course = course)
            else:
                subjects =[] 
            
        except Student.DoesNotExist:
            print('No student found for the user')
            return redirect('/') 
    return render(request, 'view_subjects.html', {'subjects': subjects})

def divisions(request):
    divisions = Division.objects.all()
    return render(request, 'adminApp/manage_division.html', {'divisions': divisions})

def courses(request):
    courses = Course.objects.all()

