# from django_filters.rest_framework import DateFromToRangeFilter, FilterSet

from posts.models import Upvote
from rest_framework.pagination import PageNumberPagination


class PaginationPosts(PageNumberPagination):
    """
    set custom pagination for list of posts
    """

    page_size = 3
    max_page_size = 1000


def post_upvotes_resetter():
    """
        Function for scheduler to reset upvote count
    """

    Upvote.objects.all().delete()
