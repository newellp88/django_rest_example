from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from .models import User, Post
from .admin import ReviewAdmin
import requests
from datetime import datetime
from rest_framework import status

# global test variables
base_url = 'http://127.0.0.1:8000/api/v1'
test_token = "c843a4eba7e96a47734da0f80daf1e8f10e3524b"
auth = "Token %s" % test_token
headers = {'Authorization': auth}


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


class CreateUserRequestTestCase(TestCase):

    def setUp(self):
        self.url = base_url + '/users/'
        self.data = {"username": "test user", "email": "example@text.com"}
        self.req = requests.post(self.url, data=self.data)

    def test_create_user_request(self):
        self.assertEqual(self.req.status_code, status.HTTP_200_OK)


class CreateReviewRequestTestCase(TestCase):

    def setUp(self):
        self.url = base_url + '/reviews/'
        self.headers = {'Authorization': auth}
        self.new_post = {'rating': 5, 'title': 'great experience with Costco',
                             'summary': 'john gave me a discount, it was great!',
                             'ip_address': '127.0.0.1', 'company': 'Costco'}
        self.req = requests.post(self.url, headers=headers, data=self.new_post)

    def test_create_review_request(self):
        self.assertEqual(self.req.status_code, status.HTTP_201_CREATED)


class GetUserReviewsTestCase(TestCase):

    def setUp(self):
        self.url = base_url + '/reviews/'
        self.req = requests.get(self.url, headers=headers)

    def test_get_user_reviews(self):
        self.assertEqual(self.req.status_code, status.HTTP_200_OK)


class ReviewAdminTestCase(TestCase):

    def setUp(self):
        self.review_admin = ReviewAdmin(Post, AdminSite())

    def test_review_admin(self):
        self.assertEqual(str(self.review_admin), 'api.ReviewAdmin')
