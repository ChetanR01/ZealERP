from django.shortcuts import render, redirect
from studentApp.models import Course
from .models import LeaveRequest,Student
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from studentApp.models import Course



def dashboard(request):
    return render(request, 'base.html')




from adminApp.models import ExtendedUser  # Import the ExtendedUser model
from studentApp.models import LeaveRequest

def apply_leave(request):
    if request.method == 'POST':
        duration_start = request.POST['duration_start']
        duration_end = request.POST['duration_end']
        reason = request.POST['reason']
        proof_image = request.FILES.get('proof_image')

        # Get the ExtendedUser instance for the current user
        try:
            student = ExtendedUser.objects.get(user=request.user)  # Assuming you have a OneToOne relationship with User
        except ExtendedUser.DoesNotExist:
            # Handle the case where the ExtendedUser doesn't exist (in case of missing data)
            return render(request, 'error.html', {'message': 'Student record not found!'})

        # Create the leave request, passing the ExtendedUser instance for student
        leave_request = LeaveRequest(
            duration_start=duration_start,
            duration_end=duration_end,
            reason=reason,
            proof_image=proof_image,
            student=student  # Assign the ExtendedUser instance
        )
        leave_request.save()

        # Redirect to the leave requests page or any other page
        return redirect('student:leave_requests')

    return render(request, 'studentapp/apply_leave.html')

def leave_request(request):
    leave_requests = LeaveRequest.objects.filter(student=request.user.student) 
    return render(request, 'studentapp/leave_request.html', {'leave_request': leave_requests})
