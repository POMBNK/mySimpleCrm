from django import forms
from .models import Lead

class ModelLeadForm(forms.ModelForm):
    '''That class allows make a form based on 'Lead' model's attributes'''
    class Meta:
        model = Lead
        fields = '__all__'


class ModelLeadFormUpdate(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'