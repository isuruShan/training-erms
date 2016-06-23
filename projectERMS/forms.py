from django import forms
from ermsapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#user registration forms start#

class user_form(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = ('username','password1','password2','first_name','last_name')

class profile_form(forms.ModelForm):
    UPhoto = forms.ImageField(label='Profile Picture')
    class Meta:
        model=Users
        exclude = ('User',)
#user registration forms end#ta

#adding degree types and hierachey form

class DegreeType_Form(forms.ModelForm):
    class Meta:
        model = DegreeType
        exclude = ()