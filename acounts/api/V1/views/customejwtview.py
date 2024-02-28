from rest_framework_simplejwt.views import TokenObtainPairView
from acounts.api.V1.serializer.customeobtainpairtoken import CustomObtainPairSerializer


class Customejwtview(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer
