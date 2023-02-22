from django import forms
from captcha.fields import CaptchaField
from .models import Comment


class CommentModelForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = (
            "user_name",
            "email",
            "home_page",
            "text",
        )

