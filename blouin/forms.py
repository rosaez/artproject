from django import forms

from .models import Painting

class PaintingForm(forms.Form):
    painter = forms.CharField(required=False)
    year = forms.CharField(required=False)
    height = forms.CharField(required=False)
    width = forms.CharField(required=False)