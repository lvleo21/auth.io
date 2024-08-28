from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models as djmodels
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group

from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

from apps.core.models import Account
from apps.core.sites import custom_admin_site


admin.site.unregister(Group)


class BaseAdmin(ModelAdmin):
    ordering = ('-created_at',)
    list_filter = ['is_active']

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }

    # Display submit button in filters
    list_filter_submit = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail

    formfield_overrides = {
        djmodels.TextField: {
            "widget": WysiwygWidget,
        }
    }


@admin.register(Account, site=custom_admin_site)
class AccountAdmin(UserAdmin, BaseAdmin):
    list_display = [
        "email", "username", "is_staff", "email_is_confirmed", "created_at",
        "is_active"
    ]
    list_filter = ["email", "is_staff", "is_active"]

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "email",
                    "username",
                    "password",
                    "first_name",
                    "last_name"
                ]
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "email_is_confirmed",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                ),
            },
        )
    ]

    list_editable = ["email_is_confirmed", "is_active"]
    search_fields = ["email"]
    ordering = ["username"]


@admin.register(Group, site=custom_admin_site)
class GroupAdmin(GroupAdmin, ModelAdmin):
    ...
