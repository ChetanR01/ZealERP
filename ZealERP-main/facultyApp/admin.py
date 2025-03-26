from django.contrib import admin
from .models import Staff, StaffLeaveApplication

# Staff Admin
admin.site.register(StaffLeaveApplication)
admin.site.register(Staff)
