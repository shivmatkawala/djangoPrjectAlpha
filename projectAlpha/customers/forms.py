from django import forms

from .models import Signup


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['custId','firstname', 'lastname', 'gender','email', 'phone', 'city', 'state']