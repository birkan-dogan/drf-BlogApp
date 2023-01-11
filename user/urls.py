from django.urls import path
from .views import RegisterView

from rest_framework.authtoken import views
# to create new token for user automatically when url is "login/""

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", views.obtain_auth_token),
]