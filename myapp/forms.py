from django import forms
from .models import Task

class introform(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ["description"]

