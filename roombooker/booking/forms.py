from django import forms
from fullcalendar.models import CalendarEvent
from django.contrib.admin import widgets                                       


class BookingForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        exclude = ['all_day']
