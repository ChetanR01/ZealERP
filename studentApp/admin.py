from django.contrib import admin
from .models import *
from studentApp.models import Course,Student
# Register your models here.


admin.site.register(Course)

admin.site.register(Student)
admin.site.register(Attendance)