from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *

class entryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content', 'date', 'time']

        widgets = {
            'date': forms.DateInput(format='%dd/%mm/%YYYY'),
        }