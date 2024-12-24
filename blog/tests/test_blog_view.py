from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, Profile
from blog.models import Post, Category
from datetime import datetime


class TestBlogView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email="test@test.com", password="123")
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="test name",
            last_name="test last",
            description="test desc",
        )
        self.post = Post.objects.create(
            author=self.profile,
            title="test",
            content="test content",
            status=True,
            category=None,
            published_date=datetime.now(),
        )

    def test_blog_index_response_200(self):
        url = reverse("blog:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(str(response.content).find("index"))
        self.assertTemplateUsed(response, template_name="index.html")

    def test_blog_post_detail_is_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_post_detail_is_anonymous_response(self):
        url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
