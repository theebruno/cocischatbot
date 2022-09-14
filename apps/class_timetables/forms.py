from django import forms

from .models import ClassTimetable


class ClassTimetableForm(forms.Form):
    course_unit_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Course Unit Name",
                "class": "form-control"
            }
        ))

    class Meta:
        model = ClassTimetable
        fields = (
            'course_unit_name',
            'course_unit_code',
            'course_unit_lecturer'
        )


class ClassTimetableEditForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = ClassTimetable
        fields = ('name',)
