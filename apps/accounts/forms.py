from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django import forms


# User = get_user_model()
# User = settings.AUTH_USER_MODEL


class SignupForm(forms.ModelForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password Confirmation",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__exact=username)

        if qs.exists():
            raise forms.ValidationError('username already taken!')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__exact=email)

        if qs.exists():
            raise forms.ValidationError('email already exists!')

        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password mismatch! Check and try again.')
        return password2

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))

        # user.is_active = False

        if commit:
            user.save()
            # auth.login(self.request, user)
            # user.profile.send_activation_email()

        return user


class LoginForm(AuthenticationForm):
    """
    foo comment
    """

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
