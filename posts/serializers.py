from rest_framework import serializers
from .models import Post, Upvote, Comment


class UpvoteListSerializer(serializers.ModelSerializer):
    """
    Serializer that is used to collect list of upvotes
    in order to be shown in list of posts
    """

    author = serializers.ReadOnlyField(source="upvoter.username")

    class Meta:
        model = Upvote
        fields = ["id", "author"]


class CommentListSerializer(serializers.ModelSerializer):
    """
    Serializer that is used to collect list of comments
    in order to be shown in list of posts
    """

    author = serializers.ReadOnlyField(source="comment_author.username")

    class Meta:
        model = Comment
        fields = ["id", "author", "content"]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    upvote_set = UpvoteListSerializer(many=True, read_only=True)
    upvotes = serializers.SerializerMethodField()
    comment_set = CommentListSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    # get the number (count) of upvotes of particular post
    def get_upvotes(self, post):
        return Upvote.objects.filter(post=post).count()

    # get the number (count) of comments of particular post
    def get_comments(self, post):
        return Comment.objects.filter(commented_on=post).count()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content"]


class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = [
            "id",
        ]
