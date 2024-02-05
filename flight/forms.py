from django import forms
from .models import Flight
from datetime import datetime

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'
        widgets = {
            'departure': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'arrival': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            )
        }


class FlightSearch(forms.Form):
    date_time = forms.DateTimeField(widget=forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control',}
            ))