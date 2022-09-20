from django.conf.urls import url
from django.contrib.auth.views import \
    LogoutView, \
    PasswordResetDoneView, \
    PasswordResetView, \
    PasswordResetConfirmView, \
    PasswordResetCompleteView, \
    PasswordChangeView
# from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView

# from .views import SignUpView, AccountLoginView, activate_user_view
from .views import SignUpView, AccountLoginView


urlpatterns = [

    # account/...
    url(r'^signup/$', SignUpView.as_view(), name='register'),

    url(r'^signup-success/$', TemplateView.as_view(
        template_name='accounts/signup_success.html'), name='signup_success'),

    url(r'^login/$', AccountLoginView.as_view(), name="login"),

    url(r'^logout/$', LogoutView.as_view(template_name='accounts/logged_out.html'), name='logout'),

    # url(r'^password-change/$', PasswordChangeView.as_view(
    #     template_name='accounts/password_change_form.html',
    #     success_url=reverse_lazy('profiles:show_self')
    # ), name='password_change'),

    # url(r'^password-reset/$',  PasswordResetView.as_view(
    #     template_name='accounts/password_reset_form.html',
    #     success_url=reverse_lazy('accounts:password_reset_done'),
    #     subject_template_name='accounts/emails/password_reset_subject.txt',
    #     email_template_name='accounts/emails/password_reset_email.html'
    # ), name='password_reset'),

    # url(r'^password-reset-done/$',
    #     PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html',
    #     ), name='password_reset_done'),
    #
    # url(r'^password-reset'
    #     r'/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$$',
    #     PasswordResetConfirmView.as_view(
    #         template_name='accounts/password_reset_confirm.html',
    #         success_url=reverse_lazy('accounts:password_reset_complete'),
    #     ), name='password-reset-confirm'),    # NOQA
    #
    # url(r'^password-reset/complete/$',
    #     PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
    #     name='password_reset_complete'),
]

