from django.contrib import admin
from .models import *
from studentApp.models import Course,Student,Division
# Register your models here.


admin.site.register(Course)
admin.site.register(Division)
admin.site.register(Student)
admin.site.register(LeaveRequest)
