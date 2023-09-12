from django import forms
from account.models import User


class RegistrationForm(forms.ModelForm):
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "id": "password_repeat"
                   }
        )
    )

    class Meta:
        model = User
        fields = ("username", "email", "password")
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "id": "username"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "id": "email"}
            ),
            "password": forms.PasswordInput(
                attrs={"class": "form-control", "id": "password"}
            )
        }

    # def clean(self):
    #     has_errors = False
    #     if len(self.cleaned_data["password"]) < 8:
    #         self.add_error("password", "Small size, make password with 8 or more symbols")
    #         has_errors = True
    #     if self.cleaned_data["password"] is not self.cleaned_data["password_repeat"]:
    #         self.add_error("password_repeat", "Password is not the same")
    #         has_errors = True
    #
    #     if has_errors:
    #         raise forms.ValidationError("Invalid form")
    #     return self.cleaned_data
