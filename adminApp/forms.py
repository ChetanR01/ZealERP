from django import forms 
from .models import Subject
from studentApp.models import Attend, Student

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["subject_code", "subject_name", "subject_type", "course_type", "course", "semester", "faculty"]

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attend
        fields = ['student', 'status']     
     
    
   