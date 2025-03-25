from django.contrib import admin

# Register your models here.
from facultyApp.models import Division

# Register your models here.
from .models import Staff

admin.site.register(Division)
admin.site.register(Staff)
