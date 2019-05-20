from django import forms
from django.forms import widgets
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model


class SignupForm(auth_forms.UserCreationForm):
    email = forms.EmailField(
        widget=widgets.EmailInput(attrs={"placeholder": "Email"}), label=""
    )
    first_name = forms.CharField(
        widget=widgets.Input(attrs={"placeholder": "First Name"}), label=""
    )
    last_name = forms.CharField(
        widget=widgets.Input(attrs={"placeholder": "Last Name"}), label=""
    )
    password1 = forms.CharField(
        widget=widgets.PasswordInput(attrs={"placeholder": "Enter Password"}), label=""
    )
    password2 = forms.CharField(
        widget=widgets.PasswordInput(attrs={"placeholder": "Confirm Password"}),
        label="",
    )

    class Meta:
        model = get_user_model()
        fields = ("email", "first_name", "last_name", "password1", "password2")


class LoginForm(auth_forms.AuthenticationForm):
    username = forms.EmailField(
        widget=widgets.EmailInput(attrs={"placeholder": "Email"}), label=""
    )
    password = forms.CharField(
        widget=widgets.PasswordInput(attrs={"placeholder": "Password"}), label=""
    )

    class Meta:
        fields = ["username", "password"]