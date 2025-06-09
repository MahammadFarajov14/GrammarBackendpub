from rest_framework.generics import ListCreateAPIView
from core.models import Check_up
from core.api.serializers import CheckUpSerializer

class CheckUpApiView(ListCreateAPIView):
    serializer_class = CheckUpSerializer
    queryset = Check_up.objects.all()