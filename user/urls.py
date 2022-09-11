from django.urls import path
from .views import MyTokenView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path("signin", MyTokenView.as_view()),
]
