from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from facultyApp.models import Staff,StaffLeaveApplication

def dashboard(request):
    return render(request, 'base.html')

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



