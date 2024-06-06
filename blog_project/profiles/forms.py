from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['about', 'author']
        labels = {
            'about': 'About',
            'author': 'Author',
        }
        widgets = {
            'about': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your bio'}),
        }
        help_texts = {
        }
        error_messages = {
            'author': {
                'required': 'This field is required.',
            },
        }