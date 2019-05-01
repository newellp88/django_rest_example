from .models import Post
from .serializers import PostSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status, authentication, permissions, viewsets
from datetime import datetime
import secrets, requests, json
from django.contrib.auth.models import User


class UserViewSet(viewsets.ViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        """
        Creates and stores a new user. Request body requires username and email parameters.
        Returns the users' authorization token which is used to access and create reviews.
        """
        username = request.data['username']
        password = secrets.token_urlsafe(15)

        # create user
        user = User.objects.create_user(username=username,
                                        email=request.data['email'],
                                        password=password)
        user.save()

        # request token for new user
        token_request = requests.post('http://127.0.0.1:8000/api/v1/api-token-auth/',
                                      data={'username': username, 'password': password})
        token = json.loads(token_request.content)['token']

        # give the token to the user
        return Response({"your api token": token})


class PostViewSet(viewsets.ViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get_ip_address(request):
        ip = request.META.get("HTTP_X_FORWARDED_FOR", request.META.get("REMOTE_ADDR")).split(',')[-1].strip()
        return ip

    def create(self, request):
        """
        Creates a new company review posting.
        'Authorization: Token <token>' header required. Request body parameters: rating
        (1-5), title, summary, company
        """
        ip = self.get_ip_address(request)
        token = request.headers['Authorization'].split(' ')[1]
        serializer = self.serializer_class(data={
            'rating': request.data['rating'], 'title': request.data['title'],
            'summary': request.data['summary'], 'ip_address': ip,
            'submission_date': datetime.now().date(), 'company': request.data['company'],
            'reviewer': token
        })

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """
        Returns a list of reviews posted by the user.
        'Authorization: Token <token>' header required.
        """
        token = request.headers['Authorization'].split(' ')[1]
        user_reviews = list(Post.objects.filter(reviewer=token).values())
        return Response({"published reviews": user_reviews})

