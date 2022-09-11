from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Account, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = "__all__"
        extra_fields = ["user"]


class MyTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        user = User.objects.filter(username=attrs['username']).get()
        pharmacy = Account.objects.filter(user=user).get()
        pharmacy_data = {
            'id': user.id, 'username': user.username, 'latitude': pharmacy.latitude, 'longitude': pharmacy.longitude, 'picture': pharmacy.picture}
        context = {
            'access': data['access'], 'refresh': data['refresh'], 'pharmacy': pharmacy_data}

        return context
