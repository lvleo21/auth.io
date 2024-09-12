from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.db.models import Q

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

from apps.core.models import Account
from apps.api import exceptions


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username_or_email = attrs.get(self.username_field)
        password = attrs.get("password")

        user: Account = (
            Account.objects.filter(
                Q(email=username_or_email) | Q(username=username_or_email)
            )
            .distinct()
            .first()
        )

        # TODO: Investigar authentication rules

        if user and not user.email_is_confirmed:
            raise exceptions.EmailNotConfirmedException()

        if user:
            user = authenticate(username=user.username, password=password)

        if not user:
            raise exceptions.AuthenticationFailed()

        refresh = self.get_token(user)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }
