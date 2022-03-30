from django.urls import path

from accounts import views

from rest_framework_simplejwt.views import TokenRefreshView
from accounts.views import MyObtainTokenPairView

urlpatterns = [
    path("api/user-list", views.UserListView.as_view()),
    path("api/user-activity", views.UserActivityListView.as_view()),
    path("api/jwt/login", MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path("api/jwt/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
