from django.shortcuts import render, redirect

from facultyApp.models import notification

from studentApp.models import Course, Student, Division
from .models import LeaveRequest

from adminApp.models import Subject
from django.contrib.auth.decorators import login_required


def dashboard(request):
    return render(request, 'base.html')

def show_notifications(request):
    notifications = notification.objects.all().order_by('-created_at')
    return render(request,"studentApp/notifications.html",{'data':notifications})


def apply_leave(request):
    if request.method == 'POST':
        duration_start = request.POST['duration_start']
        duration_end = request.POST['duration_end']
        reason = request.POST['reason']
        proof_image = request.FILES.get('proof_image')
        try:
            student = Student.objects.get(user=request.user)
        except Student.DoesNotExist:
            return render(request, 'error.html', {'message': 'Student record not found!'})
        leave_request = LeaveRequest(
            duration_start=duration_start,
            duration_end=duration_end,
            reason=reason,
            proof_image=proof_image,
            student=student
        )
        leave_request.save()
        return redirect('student:leave_request')

    return render(request, 'studentapp/apply_leave.html')


def leave_request(request):
    try:
        student = Student.objects.get(user=request.user)
        leave_requests = LeaveRequest.objects.filter(student=student)
    except Student.DoesNotExist:
        return render(request, 'error.html', {'message': 'Student record not found!'})

    return render(request, 'studentapp/leave_request.html', {'leave_requests': leave_requests})


def view_subjects(request):
    if request.user.is_authenticated:
        try:
            student = Student.objects.get(user=request.user)
            course = student.course
            if course:
                subjects = Subject.objects.filter(course=course)
            else:
                subjects = []
        except Student.DoesNotExist:
            return redirect('/')
    return render(request, 'view_subjects.html', {'subjects': subjects})


def divisions(request):
    divisions = Division.objects.all()
    return render(request, 'adminApp/manage_division.html', {'divisions': divisions})


def courses(request):
    courses = Course.objects.all()
    return render(request, 'adminApp/manage_courses.html', {'courses': courses})
