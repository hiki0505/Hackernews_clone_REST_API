
# from django_filters import rest_framework as filters

# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from .models import Post, Upvote, Comment
from .serializers import (
    PostSerializer,
    UpvoteSerializer,
    CommentSerializer,
)
from .services import PaginationPosts
from .permissions import (
    AuthorRightsPermission,
    AuthorRightsPermissionPost,
    CommentAuthorRightsPermission,
)


class PostList(generics.ListCreateAPIView):
    """
    Endpoint for creating and viewing posts

    permission_classes - list custom permissions for user who interacts with posts
    pagination_class - custom pagination class
    filter_backends - list of filter classes
    search_fields - based on this list of fields, filtering will be applied
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, AuthorRightsPermission]
    pagination_class = PaginationPosts
    filter_backends = [SearchFilter]
    search_fields = ["title", "author__username", "comment__content"]

    """ set author of post to currently logged in user """

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveDestroy(generics.RetrieveDestroyAPIView):
    """
    Endpoint for retrieving and deleting posts
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        AuthorRightsPermissionPost,
    ]

    """ 
    delete particular post that belongs to logged in user,
    preventing user from deleting other users' posts 
    """

    def delete(self, request, *args, **kwargs):
        post = Post.objects.filter(pk=self.kwargs["pk"], author=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError("This is not your post!")


class UpvoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    """
    Endpoint for upvoting and deleting upvote from posts
    """

    serializer_class = UpvoteSerializer
    permission_classes = [permissions.IsAuthenticated, AuthorRightsPermission]

    """ get the upvote, which was made by logged in user to a particular post, if exists """

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs["pk"])
        return Upvote.objects.filter(upvoter=user, post=post)

    """ create an upvote, if not upvoted already, otherwise throw an exception """

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError("You already upvoted that post")
        serializer.save(
            upvoter=self.request.user, post=Post.objects.get(pk=self.kwargs["pk"])
        )

    """ delete upvote, if upvoted already, otherwise throw an exception """

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError(
                "For deleting upvote you should first upvote the post..."
            )


class CommentCreate(generics.ListCreateAPIView, mixins.DestroyModelMixin):
    """
    Endpoint for creating a comment to particular post
    """

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, AuthorRightsPermission]

    """ get the comments, which was made by logged in user to a particular post, if exists """

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs["pk"])
        return Comment.objects.filter(comment_author=user, commented_on=post)

    """ create a comment to a particular post by logged in user """

    def perform_create(self, serializer):
        serializer.save(
            comment_author=self.request.user,
            commented_on=Post.objects.get(pk=self.kwargs["pk"]),
        )


class CommentRetrieveDestroy(generics.RetrieveDestroyAPIView):
    """
    Endpoint for retrieving and deleting comments
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        CommentAuthorRightsPermission,
    ]

    """ allow user to delete only his own comments, 
        preventing from deleting other users' comments 
    """

    def delete(self, request, *args, **kwargs):
        comment = Comment.objects.filter(
            pk=self.kwargs["pk"], comment_author=self.request.user
        )
        if comment.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(
                "You are not allowed to delete the other users' comments!"
            )
