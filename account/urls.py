from django.urls import path
from account.views import registration

urlpatterns = [path("registration/", registration, name="registration_page")]