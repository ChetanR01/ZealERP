from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    designation = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    joining_date = models.DateField()
    is_gfm = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.designation})"



class StaffLeaveApplication(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='faculty_leaves')
    reason = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    
    faculty = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_leaves')
    faculty_remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff.username} - {self.status}"  # Corrected this line
