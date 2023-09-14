from django.shortcuts import render, redirect
from django.contrib import messages
from home.forms import FeedbackForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
def home(request):
    return render(request, "home.html", {"page_tag": "home"})


def products(request):
    return render(request, "products.html", {"page_tag": "products"})

@login_required
def contact(request):
    if request.user.is_anonymous:
        return redirect("login")
    request.session["info"] = "CONTACTS"
    fform = FeedbackForm()
    if request.method == "POST":
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            # save data
            fform.save()
            messages.info(request, "Feedback was add. ")
            return redirect("contact_page")
    return render(request, "contact.html", {"fform": fform, "page_tag": "contact"})


def about(request):
    return render(request, "about.html", {"page_tag": "about"})
