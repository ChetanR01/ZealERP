from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Course)
admin.site.register(Division)
admin.site.register(Student)
admin.site.register(Attendance)