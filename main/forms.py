from dataclasses import field
from django import forms
from .models import *

class CovidDataForm(forms.ModelForm):
    Date_of_Record = forms.DateField()
    class Meta:
        model = Covid19
        fields = "__all__"
        widgets = {'Date_of_Record': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control','type' : 'date'})}
        