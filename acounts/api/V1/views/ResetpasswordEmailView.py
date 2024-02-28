from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from acounts.api.V1.serializer import (
    ResetPasswordEmailSerializer,
)              
from acounts.api.V1.views.SendSMSToken import Send_SMS

class ResetPasswordEmailView(GenericAPIView):
    serializer_class = ResetPasswordEmailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token = self.get_tokens_for_user(user)
        message = f'''
                     کاربر عزیز با لینک زیر هویت خود را تایید کنید حواستم جمع کن پنل گرونه
                            http://127.0.0.1:8000/acounts/api/V1/reset-password/{token}    
                                '''
        to=[serializer.validated_data["phone"]]
        Send_SMS(to, message)
        return Response({"detail": "email Resend for you..."})

    def get_tokens_for_user(self, user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)