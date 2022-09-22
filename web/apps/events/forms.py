from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput

from .models import Event


class EventForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Event Name",
                "class": "form-control"
            }
        ))

    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Event Location",
                "class": "form-control"
            }
        ))

    event_date = forms.CharField(widget=DatePickerInput(attrs={"type": "date"}))

    class Meta:
        model = Event
        fields = ('name', 'location', 'event_date', 'organiser', )
        widgets = {
                'date': DatePickerInput
            }


class EventEditForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Event Name",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Event
        fields = ('name',)
