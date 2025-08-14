from django import forms
from .models import Demon

class PromptForm(forms.ModelForm):
    class Meta:
        model = Demon
        fields = '__all__'
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Label Number'}),
            'Race': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Label Number'}),
            'Physical': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Label Number'}),
            'Fire': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Label Number'}),
            'Ice': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Label Number'}),
            'Electricity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Label Number'}),
            'Force': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Label Number'}),
            'Mystic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Label Number'}),
            'Level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Label Number'}),
        }