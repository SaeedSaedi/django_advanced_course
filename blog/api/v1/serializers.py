from rest_framework import serializers

from blog.models import Category, Post


# class PostSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "content",
            "status",
            "created_date",
            "published_date",
        ]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]
