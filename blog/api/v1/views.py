from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import PostSerializers, CategorySerializer
from blog.models import Post, Category
from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import mixins
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import LargeResultsSetPagination

# @api_view(["GET", "POST"])
# @permission_classes([IsAuthenticated])
# def api_post_list(request):
#     if request.method == "GET":
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializers(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class PostList(APIView):

#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializers(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PostSerializers(data=request.data)
#         serializer.is_valid()
#         serializer.save()
#         return Response(serializer.data)


# class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializers
#     queryset = Post.objects.filter(status=True)

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class PostList(ListCreateAPIView):

#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializers
#     queryset = Post.objects.filter(status=True)


# @api_view(["GET", "PUT", "DELETE"])
# def api_post_detail(request, id):
#     post = get_object_or_404(Post, pk=id, status=True)
#     if request.method == "GET":
#         serializer = PostSerializers(post)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = PostSerializers(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         post.delete()
#         return Response({"detail": "Item removed successfully"})


# class PostDetail(APIView):

#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializers

#     def get(self, request, id):
#         post = get_object_or_404(Post, pk=id, status=True)
#         serializers = self.serializer_class(post)
#         return Response(serializers.data)

#     def put(self, request, id):
#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = PostSerializers(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def delete(self, request, id):
#         post = get_object_or_404(Post, pk=id, status=True)
#         post.delete()
#         return Response({"detail": "Item removed successfully"})


# class PostDetail(
#     GenericAPIView,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
# ):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializers
#     queryset = Post.objects.filter(status=True)
#     lookup_field = "id"

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class PostDetail(RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializers
#     queryset = Post.objects.filter(status=True)
#     lookup_field = "id"


# class PostViewSet(viewsets.ModeViewSet):

#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializers
#     queryset = Post.objects.filter(status=True)
#     lookup_url_kwarg = "id"

#     def list(self, request):
#         serializer = self.serializer_class(self.queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, id=None):
#         post_object = get_object_or_404(self.queryset, pk=id)
#         serializer = self.serializer_class(post_object)
#         return Response(serializer.data)

#     def create(self, request):
#         pass


class PostModelViewSet(viewsets.ModelViewSet):

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status=True)
    lookup_url_kwarg = "id"
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "author", "status"]
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = LargeResultsSetPagination

    @action(methods=["GET"], detail=False)
    def get_ok(self, request):
        return Response({"detail": "ok"})


class CategoryModelViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
