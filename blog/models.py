from django.db import models
from account.models import User
from datetime import date
import os
from django.conf import settings
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_save, post_delete
from django.utils.safestring import mark_safe


class Tag(models.Model):
    value = models.CharField(max_length=20)
    desc = models.TextField()

    def __str__(self):
        return f"#{self.value}"

    class Meta:
        db_table = "tags"


class Post(models.Model):
    def image_path(self, filename):
        ext = filename.split(".")[-1]
        path = date.strftime(date.today(), "post/%Y/%m/%d")
        return f"{path}/{os.urandom(64).hex()}.{ext}"

    image = models.ImageField(upload_to=image_path)
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    views = models.IntegerField(validators=[], default=0)
    text = models.TextField()
    short_description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="posts")

    class Meta:
        db_table = "posts"
        verbose_name = "Post"
        ordering = ("-created", "-id")

    def admin_img(self):
        try:
            return mark_safe('<img src="{}" width="200px" />'.format(self.image.url))
        except ValueError:
            return mark_safe('<img src="{}" width="200px" />'.format(self.image))

    admin_img.short_description = "Image"
    admin_img.allow_tags = True

# @receiver(post_delete, sender=Post)
# def resave_media(sender, instance, **kwargs):
#     if instance.id is not None


@receiver(post_delete, sender=Post)
def remove_media(sender, instance, **kwargs):
    try:
        path_to_file = settings.MEDIA_ROOT / str(instance.image.path)
        path_to_file.unlink()
    except (OSError,  ValueError) as error:
        print(error)
    while True:
        path_to_file = (settings.MEDIA_ROOT / str(instance.image)).parent.absolute()
        try:
            path_to_file.rmdir()
        except OSError as error:
            break



class Comment(models.Model):
    ...
