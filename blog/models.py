from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Post(models.Model):
    """
    this is a class to define posts for blog app
    """

    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    this is a class to define categories for blog app
    """

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
