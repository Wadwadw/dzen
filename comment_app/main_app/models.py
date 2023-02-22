from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from captcha.fields import CaptchaField


class Comment(MPTTModel):
    user_name = models.CharField(max_length=255)
    email = models.EmailField()
    home_page = models.URLField()
    # captcha = CaptchaField()
    text = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )


    class MPTTMeta:
        order_insertion_by = ['user_name']