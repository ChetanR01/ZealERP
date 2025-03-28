from django.contrib import admin
from .models import Staff, StaffLeaveApplication,notification

# Staff Admin
admin.site.register(StaffLeaveApplication)
admin.site.register(Staff)
admin.site.register(notification)
