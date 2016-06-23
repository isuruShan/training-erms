from django import forms
from ermsapp.models import *

class Evaluation_Form(forms.ModelForm):
    class Meta:
        model = Person_Interview_viewer
        fields= ('Comment','Rate')

