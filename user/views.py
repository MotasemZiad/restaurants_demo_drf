from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.serializers import MyTokenSerializer


class MyTokenView(TokenObtainPairView):
    serializer_class = MyTokenSerializer
