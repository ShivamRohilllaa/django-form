from django import forms
from .models import *


class TaskForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    
