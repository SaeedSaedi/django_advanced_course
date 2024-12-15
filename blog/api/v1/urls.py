from django.urls import include, path
import blog.api.v1.views as views

app_name = "api_v1"

urlpatterns = [
    path("post/", views.api_post_list, name="post-list"),
    path("post/<int:id>/", views.api_post_detail, name="post-detail"),
]
