from django.db import models
from django.contrib.auth.models import User
from studentApp.models import Course 

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

from django.db import models

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
