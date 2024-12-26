from django.urls import include, path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("api/v1/", include("accounts.api.v1.urls")),
    path("api/v2/", include("djoser.urls")),
    path("api/v2/", include("djoser.urls.jwt")),
    path("sendmailwithcelery/", views.send_mail, name="sendmail-celery"),
    path("test/", views.test, name="test"),
]
