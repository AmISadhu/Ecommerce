from django.db import models
from django.contrib.auth.models import User


class FeedBack(models.Model):
    STATUSES = [("N", "New feedback"), ("P", "Feedback in process"), ("F", "Feedback was finished")]
    username = models.CharField(max_length=25, verbose_name="Full name")
    email = models.EmailField(verbose_name="User email")
    subject = models.CharField(max_length=40, verbose_name="Subject")
    message = models.TextField(verbose_name="Message", validators=[])
    status = models.CharField(max_length=1, choices=STATUSES, default="N", verbose_name="Feedback status")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    class Meta:
        db_table = "feedback"
        verbose_name = "Feed back"
        verbose_name_plural = "Feedbacks"

    def __str__(self):
        return self.username
