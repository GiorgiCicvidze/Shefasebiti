from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import ScopedRateThrottle
from django.contrib.auth.models import User

from .models import Profile, Post
from .serializers import ProfileSerializer, PostSerializer, UserSerializer
from .permissions import IsOwner


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'skills']


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    throttle_classes = [ScopedRateThrottle]

    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            return [IsAuthenticated(), IsOwner()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthenticatedOrReadOnly()]

    def get_throttles(self):
        if self.action == 'create':
            self.throttle_scope = 'post_create'
        return super().get_throttles()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserSearchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['username']