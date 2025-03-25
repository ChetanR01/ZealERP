from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class StudentLeaveApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    student = models.ForeignKey(
        'adminApp.ExtendedUser', 
        on_delete=models.CASCADE,
        related_name='student_leaves'  # Added related_name to prevent conflicts
    )
    faculty = models.ForeignKey(
        'adminApp.ExtendedUser', 
        on_delete=models.CASCADE,
        related_name='faculty_reviewed_leaves'  # Added related_name for clarity
    )
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    faculty_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.username if self.student else 'Unknown'} - {self.status}"

    # You can also add helper methods for better management if needed
    def is_pending(self):
        return self.status == 'Pending'


class FacultyLeaveApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    faculty = models.ForeignKey(
        'adminApp.ExtendedUser', 
        on_delete=models.CASCADE,
        related_name='faculty_leaves'  # Added related_name for clarity
    )
    admin = models.ForeignKey(
        'adminApp.ExtendedUser', 
        on_delete=models.CASCADE,
        related_name='admin_reviewed_leaves'  # Added related_name for clarity
    )
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    admin_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.faculty.username if self.faculty else 'Unknown'} - {self.status}"

    # You can also add helper methods for better management if needed
    def is_approved(self):
        return self.status == 'Approved'


class ExtendedUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True, null=False, default="default_username")
    email = models.EmailField(max_length=254, unique=True, default="default_email@example.com")
    password = models.CharField(max_length=128, null=True)
    groups = models.ManyToManyField('auth.Group', related_name='extendeduser_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='extendeduser_permissions', blank=True)