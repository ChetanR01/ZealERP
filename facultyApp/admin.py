from django.contrib import admin

from .models import Staff, notification, StaffLeaveApplication

# Register your models here.
admin.site.register(Staff)
admin.site.register(notification)
admin.site.register(StaffLeaveApplication)