from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'required': True}))
    password1 = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text=None)
    password2 = forms.CharField(label="Password confirmation", strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text=None)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
        }