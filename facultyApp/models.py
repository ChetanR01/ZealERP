from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    designation = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    joining_date = models.DateField()
    is_gfm = models.BooleanField(default=False) 

    def __str__(self):

        return f"{self.user.first_name} {self.user.last_name}"
    
class notification(models.Model):    
    sender_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    detail_des = models.TextField()
    notification_type = models.CharField(max_length=150)
    status_choice =[('Send','send'),('Read','read'),('Seen','seen'),('Unread','unread')]
    status = models.CharField(max_length=20, choices=status_choice, default='send')
    url = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sender_name} sends notification successfully"
        return f"{self.user.first_name} {self.user.last_name}({self.designation})"



    def __str__(self):
        return f"{self.name} is Division of {self.department}"

