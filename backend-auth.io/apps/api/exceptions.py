from django.utils.translation import gettext_lazy as _

from rest_framework import exceptions
from rest_framework import status


class EmailNotConfirmedException(exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Email has not been confirmed yet.")
    default_code = "email_not_confirmed"


class AuthenticationFailed(exceptions.AuthenticationFailed):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _("Username or password is invalid.")
    default_code = "invalid_credentials"
