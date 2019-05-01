from rest_framework import serializers
from .models import Post, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("rating", "title", "summary", "ip_address", "submission_date", "company", "reviewer")