
from .models import notification
from studentApp.models import Division

from django.shortcuts import render, redirect
from studentApp.models import LeaveRequest
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from facultyApp.models import Staff,StaffLeaveApplication


def dashboard(request):
    return render(request, 'base.html')

def show_fac_notification(request):
    notifications = notification.objects.all().order_by('-created_at')
    return render(request,"facultyApp/notification.html",{'data':notifications})


#Student Leave Manage Module
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


#Faculty Leave Module
def apply_leave(request):
    if request.method == 'POST':
        start_date = request.POST['duration_start']  # Changed to match model
        end_date = request.POST['duration_end']      # Changed to match model
        reason = request.POST['reason']
        
        try:
            Staff.objects.get(user=request.user)  # Check if staff record exists
        except Staff.DoesNotExist:
            return render(request, 'error.html', {'message': 'Staff record not found!'})
        
        leave_request = StaffLeaveApplication.objects.create(
            start_date=start_date,
            end_date=end_date,
            reason=reason,
            staff=request.user  # Corrected to assign User instance
        )
        return redirect('staff:faculty_leave_request')

    return render(request, 'facultyapp/apply_faculty_leave.html')

def faculty_leave_request(request):
    try:
        staff = Staff.objects.get(user=request.user)
        leave_requests = StaffLeaveApplication.objects.filter(staff=request.user)  # Corrected here
    except Staff.DoesNotExist:
        return render(request, 'error.html', {'message': 'Faculty record not found!'})

    return render(request, 'facultyapp/faculty_leave_request.html', {'leave_requests': leave_requests})


