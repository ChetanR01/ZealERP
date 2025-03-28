from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    designation = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    joining_date = models.DateField()
    is_gfm = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}({self.designation})"



