from django import forms

from .models import CourseUnit


class CourseUnitForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Course Name",
                "class": "form-control"
            }
        ))

    class Meta:
        model = CourseUnit
        fields = ('name', 'department')


class CourseUnitEditForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = CourseUnit
        fields = ('name',)


