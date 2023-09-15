from django.urls import path
from blog.views import blog, NewPost, PostsView, SinglePost

urlpatterns = [
    path("create/", NewPost.as_view(), name="new_post_page"),
    path("post/<slug:slug>/", SinglePost.as_view(), name="single_post"),
    path("", PostsView.as_view(), name="blog_page"),
]