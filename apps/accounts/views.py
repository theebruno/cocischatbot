from braces import views as bracesviews
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.conf import settings
from django.shortcuts import redirect, reverse
from django.views.generic import CreateView

from .forms import SignupForm, LoginForm
from apps.profiles.models import Profile

User = get_user_model()


class SignUpView(bracesviews.AnonymousRequiredMixin, CreateView):
    form_class = SignupForm
    template_name = 'accounts/register.html'
    success_url = '/'

    # def dispatch(self, request, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         return redirect('/')    # redirect to home...
    #     else:
    #         return super(SignUpView, self).dispatch(request, *args, **kwargs)


class AccountLoginView(bracesviews.AnonymousRequiredMixin, LoginView):
    template_name = "accounts/login.html"
    form_class = LoginForm

    def form_valid(self, form):
        return super(AccountLoginView, self).form_valid(form)
