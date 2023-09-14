from django.urls import path
from blog.views import blog, NewPost

urlpatterns = [
    path("create/", NewPost.as_view(), name="new_post_page"),
    path("blog/", blog, name="blog_page"),
]