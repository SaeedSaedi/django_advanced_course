from django.test import SimpleTestCase, TestCase
from ..forms import PostForm
from django.utils import timezone
from ..models import Category


class TestPostForm(TestCase):

    def test_post_form_with_valid_data(self):
        category_obj = Category.objects.create(name="hello")
        form = PostForm(
            data={
                "title": "test",
                "content": "test content",
                "status": True,
                "category": category_obj,
                "published_date": timezone.now().isoformat(),
            }
        )

        self.assertTrue(form.is_valid())

    def test_post_form_with_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
