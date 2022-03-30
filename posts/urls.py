from django.urls import path

from posts import views

# app_name = 'users_api'

urlpatterns = [
    path("api/posts", views.PostList.as_view()),
    path("api/posts/<int:pk>", views.PostRetrieveDestroy.as_view()),
    path("api/posts/<int:pk>/like", views.UpvoteCreate.as_view()),
    path("api/posts/<int:pk>/comment", views.CommentCreate.as_view()),
    path("api/comments/<int:pk>", views.CommentRetrieveDestroy.as_view()),
]
