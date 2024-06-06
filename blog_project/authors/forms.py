from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'phone_number', 'bio']
        labels = {
            'name': 'Name',
            'phone_number': 'phone_number',
            'bio': 'bio',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your bio'}),
        }
        help_texts = {
        }
        error_messages = {
            'name': {
                'required': 'This field is required.',
                'max_length': "This author's name is too long."
            },
            'phone_number': {
                'required': 'This field is required.',
                'max_length': "This phone number is too long."
            },
        }