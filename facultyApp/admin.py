from django.contrib import admin
from .models import Staff, notification
# Register your models here.
admin.site.register(Staff)
admin.site.register(notification)

from facultyApp.models import Division

# Register your models here.
from .models import Staff

admin.site.register(Division)
