from django import forms
from .models import Car, Service

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
