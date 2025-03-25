from django.db import models
from django.contrib.auth.models import User

class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USER_LIST = [("admin", 'Admin'), ('student', 'Student'), ('staff', 'Staff')]
    user_type = models.CharField(max_length=255, choices=USER_LIST, default='student')
    
    def __str__(self):
        return self.user.first_name
    
    

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

