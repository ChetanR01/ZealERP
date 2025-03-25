from django.contrib import admin
from .models import StudentLeaveApplication, FacultyLeaveApplication

@admin.register(StudentLeaveApplication)
class StudentLeaveAdmin(admin.ModelAdmin):
    list_display = ['student', 'faculty', 'start_date', 'end_date', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['student__username']

@admin.register(FacultyLeaveApplication)
class FacultyLeaveAdmin(admin.ModelAdmin):
    list_display = ['faculty', 'admin', 'start_date', 'end_date', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['faculty__username']