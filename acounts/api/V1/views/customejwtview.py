from rest_framework_simplejwt.views import TokenObtainPairView
from acounts.api.V1.serializers.customeobtainpairtoken import CustomObtainPairSerializer



class Customejwtview(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer