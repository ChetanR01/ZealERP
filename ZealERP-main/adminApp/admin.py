from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# Active user model reference
User = get_user_model()

# Extended user
class Extended_userInline(admin.StackedInline):
    model =ExtendedUser
    can_delete = False
    verbose_name_plural = 'ExtendedUsers' 

class CustomizedUserAdmin(UserAdmin):
    inlines = (Extended_userInline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
# admin.site.register(Admin)

admin.site.register(Subject)

#Custom Actions for Leave Approval/Rejection
@admin.action(description='Approve selected leaves')
def approve_leaves(modeladmin, request, queryset):
    queryset.update(status='Approved')
    messages.success(request, "Selected leave applications have been approved successfully.")

@admin.action(description='Reject selected leaves')
def reject_leaves(modeladmin, request, queryset):
    queryset.update(status='Rejected')
    messages.error(request, "Selected leave applications have been rejected.")

# Student Leave Admin
class StudentLeaveAdmin(admin.ModelAdmin):
    list_display = ['student', 'faculty', 'start_date', 'end_date', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['student__user__username']
    actions = [approve_leaves, reject_leaves]  # Added custom actions

# Faculty Leave Admin
@admin.register(FacultyLeaveApplication)
class FacultyLeaveAdmin(admin.ModelAdmin):
    list_display = ['faculty', 'admin', 'start_date', 'end_date', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['faculty__user__username']
    actions = [approve_leaves, reject_leaves]  # Added custom actions