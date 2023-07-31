from django.core import validators
from django import forms
from .models import Users,Employees

class LabourRegistration(forms.ModelForm):
    class Meta:
        model=Users
        fields=['fullname','aadhar','contact','password']
        widgets={
            'fullname': forms.TextInput(attrs={'class':'form-control'}),
            'aadhar': forms.NumberInput(attrs={'class':'form-control'}),
            'contact': forms.NumberInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }


class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model=Employees
        fields=['fullname','email','contact','password']
        widgets={
            'fullname': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'contact': forms.NumberInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }