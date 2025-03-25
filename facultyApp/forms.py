from django import forms
from .models import FacultyLeaveRequest

class FacultyLeaveRequestForm(forms.ModelForm):
    class Meta:
        model = FacultyLeaveRequest
        fields = ['leave_type', 'start_date', 'end_date', 'reason']
    
    # Explicitly defining form fields is unnecessary, as they are already defined in the model
    # So the following lines are not needed unless you want to customize the widget appearance or add validations:
    
    leave_type = forms.ChoiceField(choices=FacultyLeaveRequest.LEAVE_TYPE_CHOICES)  # Ensure LEAVE_TYPE_CHOICES is defined in the model
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    reason = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Reason for leave'}))

