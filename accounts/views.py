from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from accounts.serializers import UserInfoSerializer, UserActivitySerializer

from accounts.serializers import CustomTokenSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CustomTokenSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer
    filter_backends = [SearchFilter]
    search_fields = ["username", "email"]


class UserActivityListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserActivitySerializer
