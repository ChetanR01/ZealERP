
from .models import notification
from studentApp.models import Division

from django.shortcuts import render, redirect
from studentApp.models import LeaveRequest
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def dashboard(request):
    return render(request, 'base.html')

def show_fac_notification(request):
    notifications = notification.objects.all().order_by('-created_at')
    return render(request,"facultyApp/notification.html",{'data':notifications})

@login_required
def manage_leave(request):
    leave_requests = LeaveRequest.objects.filter(status='pending')
    return render(request, 'facultyapp/manage_leaves.html', {'leave_requests': leave_requests})

@login_required
def approve_leave(request, leave_id):
    try:
        leave_request = LeaveRequest.objects.get(id=leave_id)
        if not hasattr(request.user, 'staff') or not request.user.staff.is_gfm:
            return HttpResponse("You do not have the necessary permissions to approve leaves.", status=403)

        leave_request.status = 'approved'
        leave_request.approved_by = request.user.staff
        leave_request.save()

        return redirect('staff:manage_leave')
    except LeaveRequest.DoesNotExist:
        return HttpResponse("Leave request not found.", status=404)

@login_required
def reject_leave(request, leave_id):
    try:
        leave_request = LeaveRequest.objects.get(id=leave_id)
        leave_request.status = 'rejected'
        leave_request.save()
        return redirect('staff:manage_leave')
    except LeaveRequest.DoesNotExist:
        return HttpResponse("Leave request not found.", status=404)
      
def divisions(request):
    divisions = Division.objects.all()
    return render(request, 'adminApp/manage_division.html', {'divisions': divisions})
