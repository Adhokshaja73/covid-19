from dataclasses import field
from django import forms
from . import models

class CovidDataForm(forms.ModelForm):
    Date_of_Record = forms.DateField()
    class Meta:
        model = models.Covid19
        fields = "__all__"
        widgets = { "Date_of_Record": forms.DateInput(format=('%m/%d/%Y'),  attrs={'type' : 'date'})}
        