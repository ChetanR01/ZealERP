from django.shortcuts import render, redirect
from studentApp.models import LeaveRequest
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Division  # Corrected import path

# Create your views here.

def dashboard(request):
    return render(request, 'base.html')



@login_required
def manage_leave(request):
    leave_requests = LeaveRequest.objects.filter(status='pending')  # Only pending requests
    return render(request, 'staff/manage_leave.html', {'leave_requests': leave_requests})

@login_required
def approve_leave(request, leave_id):
    leave_request = LeaveRequest.objects.get(id=leave_id)
    leave_request.status = 'approved'
    leave_request.approved_by = request.user.staff  
    leave_request.save()
    return redirect('staff:manage_leave')

@login_required
def reject_leave(request, leave_id):
    leave_request = LeaveRequest.objects.get(id=leave_id)
    leave_request.status = 'rejected'
    leave_request.save()
    return redirect('staff:manage_leave')
def divisions(request):
    divisions = Division.objects.all()
    return render(request, 'adminApp/manage_division.html', {'divisions': divisions})
