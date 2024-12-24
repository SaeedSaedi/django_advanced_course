from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from ..views import IndexView, PostDetail, PostList

# Create your tests here.


class TestUrl(SimpleTestCase):

    def test_blog_index_url_resolve(self):
        url = reverse("blog:index")
        self.assertEqual(resolve(url).func.view_class, IndexView)

    def test_blog_list_url_resolve(self):
        url = reverse("blog:post")
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_blog_post_detail_url_resolve(self):
        url = reverse("blog:post-detail", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, PostDetail)
