from django.db import models
from django.contrib.auth.models import User
from studentApp.models import Course 
from django.conf import settings

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

class Subject(models.Model):
    SUBJECT_TYPES = [
        ('Core', 'Core'),
        ('Elective', 'Elective'),
    ]

    COURSE_TYPES = [
        ('Theory', 'Theory'),
        ('Lab', 'Lab')
    ]
    
    subject_code = models.CharField(max_length=20, unique=True)
    subject_name = models.CharField(max_length=100)
    subject_type = models.CharField(max_length=10, choices=SUBJECT_TYPES)
    course_type = models.CharField(max_length=10, choices=COURSE_TYPES)
    semester = models.IntegerField()
    faculty = models.CharField(max_length=100)  # Change to ForeignKey if linking to a Faculty model
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="subjects", null=True, blank=True)


    def __str__(self):
        return f"{self.subject_code} - {self.subject_name}"

class FacultyLeaveApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    faculty = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='admin_faculty_leaves'  # Added related_name for clarity
    )
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
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

    def is_approved(self):
        return self.status == 'Approved'