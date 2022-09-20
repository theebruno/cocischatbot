from django import forms

from .models import Course


class CourseForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Course Name",
                "class": "form-control"
            }
        ))
    # department = forms.Select()

    class Meta:
        model = Course
        fields = ('name', 'department')


class CourseEditForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Course Name",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Course
        fields = ('name',)


