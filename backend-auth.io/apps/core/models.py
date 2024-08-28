import re
import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core import validators

from apps.core.managers import AccountManager


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Criado em"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Atualizado em"))
    is_active = models.BooleanField(
        verbose_name=_("Está ativo?"), default=True,
        help_text=_('Designa se este usuário está ativo na plataforma.')
    )

    class Meta:
        abstract = True


class Account(BaseModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _("Nome de usuário"),
        max_length=15,
        unique=True,
        help_text=_(
            "Obrigatório. Máximo de 15 caracteres. Letras, números e caracteres @/./+/-/_ permitidos."
        ),
        validators=[
            validators.RegexValidator(
                re.compile("^[\w.@+-]+$"),
                _("Insira um nome de usuário válido."),
                "invalid",
            )
        ],
    )
    password = models.CharField(_("Senha"), max_length=128)
    first_name = models.CharField(_("Nome"), max_length=30, null=True, blank=True)
    last_name = models.CharField(_("Sobrenome"), max_length=30, null=True, blank=True)
    email = models.EmailField(_("E-mail"), max_length=255, unique=True)
    email_is_confirmed = models.BooleanField(
        _("E-mail está confirmado"),
        default=False,
        help_text=_("Designa se este usuário confirmou seu e-mail."),
    )
    is_staff = models.BooleanField(
        _("É Staff?"),
        default=False,
        help_text=_(
            "Designa se o usuário pode efetuar login neste site de administração."
        ),
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = AccountManager()

    class Meta:
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")

    @property
    def full_name(self):
        full_name = f"{self.first_name or ''} {self.last_name or ''}"

        if full_name.strip() == "":
            return self.username

        return full_name.strip()
