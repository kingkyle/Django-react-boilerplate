from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Accounts


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Accounts
        fields = ('first_name', 'last_name', 'email', 'reg_ip')
        widgets = {'reg_ip': forms.HiddenInput}

    def clean_password2(self):
        # Check to see if the two password entries match
        password = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise forms.ValidationError("Password do not match!")
        return password2

    def save(self, commit=True):
        # Hash the provided Password
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean(self):
        email = self.cleaned_data.get("email")
        if email and Accounts.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Email Address is already in use")
        return email


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on the user, but replaces the password field with admin's
        password hash display field."""

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Accounts
        fields = ('email', 'first_name', 'last_name',
                  'is_active', 'is_staff', 'is_superuser')

    def clean_password(self):
        return self.initial["password"]
