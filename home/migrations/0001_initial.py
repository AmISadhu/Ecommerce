# Generated by Django 4.2.1 on 2023-06-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FeedBack",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("username", models.CharField(max_length=25, verbose_name="Full name")),
                ("email", models.EmailField(max_length=254, verbose_name="User email")),
                ("subject", models.CharField(max_length=25, verbose_name="Subject")),
                ("message", models.TextField(verbose_name="Message")),
                (
                    "status",
                    models.CharField(
                        choices=[("N", "New feedback"), ("P", "Feedback in process"), ("F", "Feedback was process")],
                        default="N",
                        max_length=1,
                        verbose_name="Feedback status",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Created")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Last Updated")),
            ],
            options={"verbose_name": "Feed back", "verbose_name_plural": "Feedbacks", "db_table": "feedback"},
        )
    ]
