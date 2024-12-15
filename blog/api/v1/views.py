from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializers
from blog.models import Post
from rest_framework import status


@api_view(["GET", "POST"])
def api_post_list(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view()
def api_post_detail(request, id):

    try:
        post = Post.objects.get(pk=id)
        serializer = PostSerializers(post)

        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response("Not found", status=status.HTTP_404_NOT_FOUND)
