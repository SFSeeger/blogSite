from django import forms

class SignUP(forms.Form):
    name = forms.CharField(max_length=25)
    username = forms.CharField(max_length=25)
    email = forms.EmailField()
    password = forms.CharField(max_length=60)
    password2 = forms.CharField(max_length=60)
