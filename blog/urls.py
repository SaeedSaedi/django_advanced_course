from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("post/", views.PostList.as_view(), name="post"),
    path("post/<int:pk>", views.PostDetail.as_view(), name="post-detail"),
]
