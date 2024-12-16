from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import PostSerializers
from blog.models import Post
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView
from rest_framework import mixins

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


class PostList(ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status=True)


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


class PostDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers

    def get(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        serializers = self.serializer_class(post)
        return Response(serializers.data)

    def put(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = PostSerializers(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({"detail": "Item removed successfully"})
