from django import forms
from django.db import models
from listings.models import Sign

class SingForm(forms.ModelForm):
    class Meta:
        model = Sign
        widgets = {
            'password': forms.PasswordInput(),
            'confirmation': forms.PasswordInput(),
        }
        fields = '__all__'

class LogForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    choix = forms.RadioSelect()

class Chifoumi(forms.Form):
    CHOICES = [
        ('pierre', 'Pierre'),
        ('feuille', 'Feuille'),
        ('ciseau', 'Ciseau'),
    ]
    votre_choix = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
    )