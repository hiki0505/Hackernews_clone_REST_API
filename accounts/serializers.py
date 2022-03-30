from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


class CustomTokenSerializer(TokenObtainPairSerializer):
    """
    This is custom token generator, which is used
    to create token that contains user info
    """

    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenSerializer, cls).get_token(user)
        print(token)
        # Add custom claims
        token["username"] = user.username
        print(user)
        # user.last_login = now()
        user.save()
        return token


class UserInfoSerializer(serializers.ModelSerializer):
    """
    User info serializer, used to represent list of users
    """

    class Meta:
        model = User
        fields = ["id", "username", "email"]


class UserActivitySerializer(serializers.ModelSerializer):
    """
    User activity serializer, used for tracking each user activity,
    by counting number of likes and comments they made
    """

    num_of_likes = serializers.SerializerMethodField()
    num_of_comments = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "num_of_likes", "num_of_comments"]

    def get_num_of_likes(self, obj):
        return obj.upvote_set.count()

    def get_num_of_comments(self, obj):
        return obj.comment_set.count()
