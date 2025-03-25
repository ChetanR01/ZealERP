from django.contrib import admin
from django.contrib.auth.decorators import login_required
from .models import Course, Division  # Explicit import ensures correctness

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'is_active']
    search_fields = ['name']

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name', 'course']
    search_fields = ['name']
'''
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'enrollment_number', 'course', 'division']
    list_filter = ['course', 'division']
    search_fields = ['user__username', 'enrollment_number']
'''

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