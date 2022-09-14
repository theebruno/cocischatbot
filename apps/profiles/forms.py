from django import forms
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, help_text=None)
    first_name = forms.CharField(max_length=20, help_text=None, required=False)
    last_name = forms.CharField(max_length=20, help_text=None, required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
        )


class ProfileEditForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Add a little description of who you are here.',
    }), label='About you')

    # profile_cover = forms.ImageField(
    #     label='Change your profile cover here', required=False)

    class Meta:
        model = Profile
        fields = (
            # 'profile_cover',
            # 'profile_pic',
            'bio',
            'phone_number',
            'office',
            'email'
        )
