from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "image", "text", "author", "short_description")
        widgets = {"author": forms.HiddenInput(),
                   "short_description": forms.HiddenInput()
                   }

    # def set_author(self, user):
    #     self.cleaned_data["author"] = user

    def clean(self):
        self.cleaned_data["short_description"] = self.cleaned_data["text"][:15] + " ..."
        return self.cleaned_data

