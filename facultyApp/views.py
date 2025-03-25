from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import FacultyLeaveRequestForm  # Ensure the correct import
from .models import FacultyLeaveRequest  # Ensure both models are imported

# Dashboard View
def dashboard(request):
    return render(request, 'base.html')

@login_required
def apply_leave(request):
    if request.method == 'POST':
        form = FacultyLeaveRequestForm(request.POST, request.FILES)
        if form.is_valid():
            leave_request = form.save(commit=False)
            
            # Correct faculty reference
            if hasattr(request.user, 'faculty'):
                leave_request.faculty = request.user.faculty
            else:
                leave_request.faculty = request.user  # Assuming `request.user` itself is the faculty
            
            leave_request.status = 'Pending'  # Default status as 'Pending'
            leave_request.save()
            return redirect('faculty:leave_requests')  # Redirect to leave requests page
    else:
        form = FacultyLeaveRequestForm()

    return render(request, 'facultyApp/apply_faculty__leave.html', {'form': form})

@login_required
def leave_requests(request):
    # Corrected faculty reference
    if hasattr(request.user, 'faculty'):
        leave_requests = FacultyLeaveRequest.objects.filter(faculty=request.user.faculty)
    else:
        leave_requests = FacultyLeaveRequest.objects.filter(faculty=request.user)

    return render(request, 'facultyApp/faculty_leave_requests.html', {'leave_requests': leave_requests})

def faculty_leave_list(request):
    leaves = FacultyLeaveRequest.objects.all()
    return render(request, 'facultyApp/faculty_leave_list.html', {'leaves': leaves})

def approve_reject_staff_leave(request, leave_id):
    leave_request = get_object_or_404(StaffLeaveRequest, id=leave_id)  # Corrected to use StaffLeaveRequest model
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            leave_request.status = 'Approved'
        elif action == 'reject':
            leave_request.status = 'Rejected'
        leave_request.save()
    return redirect('faculty_leave_list')

