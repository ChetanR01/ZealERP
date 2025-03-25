from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Course Model
class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()  # Added field
    is_active = models.BooleanField(default=True)  # Added field

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use custom user model
    enrollment_number = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    division = models.CharField(max_length=100, null=False, default='Unknown')

    def __str__(self):
        return self.user.username

class Division(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class LeaveRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='leave_requests') 
    duration_start = models.DateField() 
    duration_end = models.DateField() 
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    proof_image = models.FileField(upload_to='leave_requests/proofs/', null=True, blank=True)  # Optional proof (image/PDF)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def leave_duration(self):
        return (self.duration_end - self.duration_start).days + 1

    def _str_(self):
        return f"Leave request by {self.student.user.first_name} {self.student.user.last_name} on {self.leave_date} ({self.status})"