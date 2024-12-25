from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User, Profile
from blog.models import Post, Category
from django.utils import timezone

category_list = [
    "it",
    "design",
    "fun",
]


class Command(BaseCommand):
    help = "insert data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(), password="Test@123456")
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=3)
        profile.save()

        for name in category_list:
            Category.objects.get_or_create(name=name)

        for _ in range(10):
            Post.objects.create(
                author=profile,
                image="image/test.png",
                title=self.fake.text(max_nb_chars=25),
                content=self.fake.paragraph(nb_sentences=5),
                status=True,
                published_date=timezone.now(),
            )
