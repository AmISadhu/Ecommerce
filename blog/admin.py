from django.contrib import admin
from blog.models import Post, Tag


class AdminPost(admin.ModelAdmin):
    list_display = ("admin_img", "author")
    readonly_fields = ("admin_img", "created", "updated", "views", "author")
    list_filter = ("author", "tags")
    search_fields = ("title", "short_description", "text", "tags")
    fields = ("admin_img", "title", "author", "tags", "created", "updated", "views")


admin.site.register(Tag)
admin.site.register(Post, AdminPost)
