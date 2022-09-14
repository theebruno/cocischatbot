from django import forms

from .models import ExamTimetable


class ExamTimetableForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Course Name",
                "class": "form-control"
            }
        ))

    class Meta:
        model = ExamTimetable
        fields = ('name', 'department')


class ExamTimetableEditForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = ExamTimetable
        fields = ('name',)


