from .serializer import *
from rest_framework.views import APIView

class DestroyAuthToken(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
