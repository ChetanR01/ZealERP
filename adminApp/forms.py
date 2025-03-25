from django import forms
from .models import StudentLeaveApplication, FacultyLeaveApplication

class StudentLeaveApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentLeaveApplication
        fields = ['start_date', 'end_date', 'reason']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'reason': forms.Textarea(attrs={'rows': 4}),
        }

class FacultyLeaveApplicationForm(forms.ModelForm):
    class Meta:
        model = FacultyLeaveApplication
        fields = ['start_date', 'end_date', 'reason']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'reason': forms.Textarea(attrs={'rows': 4}),
        }
