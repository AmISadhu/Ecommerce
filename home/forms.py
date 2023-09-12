from django import forms
from home.models import FeedBack


class FeedbackForm(forms.Form):
    username = forms.CharField(
        label="Full Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "contact_name",
                "placeholder": "Contact Name"
            }
        )
    )
    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(
            attrs={"class": "form-control",
                   "id": "email",
                   "placeholder": "Email",
                   "pattern": "[^ @]*@[^ @]*"
                   }
        )
    )
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "subject",
                "placeholder": "Your subject"
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "message",
                "placeholder": "Describe message here"
            }
        )
    )

    def clean(self):
        has_errors = False
        if len(self.cleaned_data["message"]) > 20:
            self.add_error("message", "A lot of size")
            has_errors = True
        if len(self.cleaned_data["subject"]) > 10:
            self.add_error("subject", "A lot of size")
            has_errors = True

        if has_errors:
            raise forms.ValidationError("Invalid form")
        return self.cleaned_data

    def save(self):
        FeedBack.objects.create(**self.cleaned_data)
