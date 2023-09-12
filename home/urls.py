from django.urls import path
from home.views import home, products, contact, about


urlpatterns = [
    path("", home, name="home_page"),
    path("products/", products, name="products_page"),
    path("contact/", contact, name="contact_page"),
    path("about/", about, name="about_page"),
]
