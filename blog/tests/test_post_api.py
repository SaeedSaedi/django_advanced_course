import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.utils import timezone
from accounts.models import User
from blog.models import Category
import json


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def test_user():
    user = User.objects.create_user(
        email="test@test.com", password="123", is_verified=True
    )
    return user


@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_200(self, api_client):

        url = reverse("blog:index")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_request_401_status(self, api_client):
        url = reverse("blog:api_v1:post-list")
        data = {
            "title": "test",
            "content": "test content",
            "status": True,
            "published_date": timezone.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_request_200_status(self, api_client, test_user):
        category_obj = Category.objects.create(name="hello")
        url = reverse("blog:api_v1:post-list")
        data = {
            "title": "string",
            "content": "string",
            "status": True,
            "category": category_obj.id,
            "published_date": "2024-12-24T12:35:50.838Z",
        }
        api_client.force_login(user=test_user)
        response = api_client.post(url, data)
        print(response.data)
        assert response.status_code == 201
