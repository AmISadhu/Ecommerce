from django.shortcuts import render, redirect
from django.urls import reverse
from blog.forms import PostForm
from django.http.response import HttpResponseForbidden
from django.views.generic import ListView, FormView


def blog(request):
    return render(request, "blog.html", {"page_tag": "blog"})


# def new_post(request):
# if not request.user.is_authenticated:
#     return HttpResponseForbidden(content="Permission denied")
#     context = {"post_form": PostForm()}
#     if request.method == "POST":
#         user_data = request.POST.copy()
#         user_data["author"] = request.user
#         form = PostForm(user_data, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("home_page")
#         context["post_form"] = form
#     return render(request, "new_post.html", context)


class NewPost(FormView):
    template_name = "new_post.html"
    form_class = PostForm

    def get_form_kwargs(self):
        kwargs = {
            "initial": self.get_initial(),
            "prefix": self.get_prefix(),
        }
        if self.request.method in ("POST", "PUT"):
            user_data = self.request.POST.copy()
            user_data["author"] = self.request.user
            kwargs.update(
                {
                    "data": user_data,
                    "files": self.request.FILES,
                }
            )
        return kwargs

    def get_success_url(self):
        return self.request.GET.get("next", reverse("home_page"))

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
