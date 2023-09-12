from django.contrib import admin
from home.models import FeedBack


class AdminFeedback(admin.ModelAdmin):
    list_display = ("username", "status", "updated")


admin.site.register(FeedBack, AdminFeedback)
