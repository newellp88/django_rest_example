from django.test import TestCase
from .models import User, Post
from datetime import datetime

test_token = "384e68012ba53c927873d36522285a975439e63e"


class UserModelTestCase(TestCase):

    def setUp(self):
        self.username = "test user"
        self.email = "test@email.com"
        self.user = User(username=self.username, email=self.email)

    def test_user_model(self):
        old_count = User.objects.count()
        self.user.save()
        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)


class PostModelTestCase(TestCase):

    def setUp(self):
        self.new_post = Post(rating=5, title='great experience with Costco',
                             summary='john gave me a discount, it was great!',
                             ip_address='127.0.0.1', submission_date=datetime.now().date(),
                             company='Costco', reviewer=test_token)

    def test_post_model(self):
        old_count = Post.objects.count()
        self.new_post.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)
