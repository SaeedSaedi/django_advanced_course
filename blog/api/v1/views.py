from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializers
from blog.models import Post
from rest_framework import status


@api_view(["GET"])
def api_post_list(request):
    posts = Post.objects.filter(status=True)
    serializer = PostSerializers(posts, many=True)
    return Response(serializer.data)


@api_view()
def api_post_detail(request, id):

    try:
        post = Post.objects.get(pk=id)
        serializer = PostSerializers(post)

        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response("Not found", status=status.HTTP_404_NOT_FOUND)
