from .models import Teacher
from django import forms

class Taskfom(forms.ModelForm):
    class Meta:
        model = Teacher
        fields=['first_name', 'last_name', 'profile_picture', 'email_address', 'phone_number','room_number',
                'subject_taught']
