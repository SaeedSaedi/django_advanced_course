from django.urls import include, path
from . import views
from django.views.generic import TemplateView

app_name = "blog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("post/", views.PostList.as_view(), name="post"),
    path("post/<int:pk>", views.PostDetail.as_view(), name="post-detail"),
    path("api/v1/", include("blog.api.v1.urls")),
]
