from django import forms

class StudentLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your first name and last 4 digits of your NSHE number'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your 9-digit NSHE number',
        'pattern': '\d{9}'
    }))

class StudentRegistrationForm(forms.Form):
    CSN_email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your CSN student email'
    }))
    First_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your first name'
    }))
    Last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your last name'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your 9-digit NSHE number',
        'pattern': '\d{9}'
    }))

class FacultyRegistrationForm(forms.Form):
    CSN_email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your CSN faculty email'
    }))
    First_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your first name'
    }))
    Last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your last name'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password'
    }))