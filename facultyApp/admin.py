from django.contrib import admin
from .models import Staff, FacultyLeaveRequest, LeaveReportStaff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['user', 'department', 'contact_number']
    search_fields = ['user__username', 'department']

@admin.register(FacultyLeaveRequest)
class FacultyLeaveRequestAdmin(admin.ModelAdmin):
    list_display = ['faculty', 'leave_type', 'start_date', 'end_date', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['faculty__username']

@admin.register(LeaveReportStaff)  # Corrected this to LeaveReportStaff
class LeaveReportStaffAdmin(admin.ModelAdmin):
    list_display = ['staff', 'start_date', 'end_date', 'status']
    list_filter = ['status']
    search_fields = ['staff__user__username']
