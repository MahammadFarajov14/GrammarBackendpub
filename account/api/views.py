from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
    )
from drf_yasg.utils import swagger_auto_schema
from account.api.serializers import UserAPIProfileSerializer, UserTokenRefreshSerializer

class UserTokenObtainPairView(TokenObtainPairView):

    @swagger_auto_schema(responses={200: UserAPIProfileSerializer(many=True)})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class UserTokenRefreshView(TokenRefreshView):

    @swagger_auto_schema(responses={200: UserTokenRefreshSerializer(many=True)})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)