from django.urls import include, path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

app_name = "api_v1"

urlpatterns = [
    path("registration/", views.RegistrationApiView.as_view(), name="registration"),
    path("token/login/", ObtainAuthToken.as_view(), name="token-login"),
]
