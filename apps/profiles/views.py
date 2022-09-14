"""
views file for the profiles of the application
"""
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, get_list_or_404, redirect, reverse
from django.views.generic import TemplateView, ListView, View

from .forms import ProfileEditForm, UserForm
from .models import Profile

User = get_user_model()


class ProfileDetailView(LoginRequiredMixin, TemplateView):
    template_name = "profiles/profile.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            profile = get_object_or_404(Profile, slug=slug)
            user = profile.user
            kwargs['user'] = user
        else:
            user = self.request.user

        if user == self.request.user:
            kwargs["editable"] = True
        kwargs["show_user"] = user
        return super(ProfileDetailView, self).get(request, *args, **kwargs)


class EditProfile(LoginRequiredMixin, TemplateView):
    # template_name = "profiles/edit_profile.html"
    template_name = "profiles/profile.html"

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "user_form" not in kwargs:
            kwargs["user_form"] = UserForm(instance=user)
        if "profile_form" not in kwargs:
            kwargs["profile_edit_form"] = ProfileEditForm(instance=user.profile)
        return super(EditProfile, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileEditForm(request.POST, request.FILES,
                                       instance=user.profile)
        if not (user_form.is_valid() and profile_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            user_form = UserForm(instance=user)
            profile_form = ProfileEditForm(instance=user.profile)
            return super(EditProfile, self).get(request, user_form=user_form,
                                                profile_form=profile_form)
        # Both forms are fine. Time to save!
        user_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        messages.success(request, "Profile details saved!")

        return redirect(reverse("profiles:show_self"))
