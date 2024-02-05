from .models import TicketBooking
from django import forms

class TicketBookingForm(forms.ModelForm):

    class Meta:
        model = TicketBooking
        fields = ['first_name','last_name','mobile_no','class_type']