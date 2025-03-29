from django import forms 
from .models import Subject 

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["subject_code", "subject_name", "subject_type", "course_type", "course", "semester", "faculty"]

        
     
    
   