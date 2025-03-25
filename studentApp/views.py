from django.shortcuts import render, redirect
from studentApp.models import Course
from .models import LeaveRequest
from .forms import LeaveRequestForm
from django.contrib.auth.decorators import login_required


def dashboard(request):
    return render(request, 'base.html')



def apply_leave(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST, request.FILES)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.student = request.user.student 
            leave_request.save()
            return redirect('student:leave_requests') 
    else:
        form = LeaveRequestForm()
    return render(request, 'studentapp/apply_leave.html', {'form': form})


def leave_request(request):
    leave_requests = LeaveRequest.objects.filter(student=request.user.student) 
    return render(request, 'studentapp/leave_request.html', {'leave_request': leave_requests})