from django.urls import include, path
import blog.api.v1.views as views
from rest_framework.routers import DefaultRouter

app_name = "api_v1"

router = DefaultRouter()
router.register("post", views.PostModelViewSet, "post")
router.register("category", views.CategoryModelViewSet, "category")

urlpatterns = router.urls

# urlpatterns = [
#     # path("post/", views.api_post_list, name="post-list"),
#     # path("post/", views.PostList.as_view(), name="post-list"),
#     # path("post/<int:id>/", views.api_post_detail, name="post-detail"),
#     # path("post/<int:id>/", views.PostDetail.as_view(), name="post-detail"),
#     path(
#         "post/",
#         views.PostViewSet.as_view({"get": "list", "post": "create"}),
#         name="post-list",
#     ),
#     path(
#         "post/<int:id>/",
#         views.PostViewSet.as_view({"get": "retrieve"}),
#         name="post-list",
#     ),
# ]
