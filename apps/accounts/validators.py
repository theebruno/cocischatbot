from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class AllAlphabeticPasswordValidator(object):
    """
    Validate whether the password is alphabetic.
    """
    def validate(self, password, user=None):

        if password.isalpha():
            raise ValidationError(
                _("This password is entirely alphabetic."),
                code='password_entirely_alphabetic',
            )

    def get_help_text(self):
        return _("Your password can't contain alphabetic letters only.")
