from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as BaseLoginView
from account.forms import RegistrationForm


def registration(request):
    rform = RegistrationForm()
    if request.method == "POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            rform.save()
            return redirect("login")
    return render(request, "account.html", {"rform": rform})


# class LoginView(BaseLoginView):
#     ...
