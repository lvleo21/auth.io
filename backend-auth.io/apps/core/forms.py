from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.core.models import Account


class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=60)

    class Meta:
        model = Account
        fields = ["email", "username", "name", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if "name" in self.changed_data:
            name = self.cleaned_data["name"].split(" ")

            user.first_name = name[0]
            user.last_name = " ".join(name[1:])

        if commit:
            user.save()

        return user
