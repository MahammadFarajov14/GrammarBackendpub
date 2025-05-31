from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password'
        )

class UserAPIProfileSerializer(serializers.ModelSerializer):

    refresh = serializers.CharField()
    access = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'refresh',
            'access',
            'id',
            'username',
            'password',
        )

class UserTokenRefreshSerializer(serializers.ModelSerializer):

    access = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'access',
        )

class UserTokenPairSeializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        user_serializer = UserProfileSerializer(self.user)
        data.update(user_serializer.data)
        return data