from django import forms
from .models import AdoptionForm

class AdoptionFormForm(forms.ModelForm):
    class Meta:
        model = AdoptionForm
        fields = ['message']
