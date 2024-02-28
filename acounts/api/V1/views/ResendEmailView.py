from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from acounts.api.V1.serializer import (
    ResendEmailSerializer,
)              
from acounts.api.V1.views.SendSMSToken import Send_SMS

class ResendEmailView(GenericAPIView):
    '''Resend Email  to user  for verification '''
    serializer_class = ResendEmailSerializer

    def post(self, request, *args, **kwargs):
        ''' This method is used to resend email to user  for verification '''
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        if user.is_verified:
            return Response({"detail": "your phone is already verified"})
        token = self.get_tokens_for_user(user)
        message = f'''
                     کاربر عزیز با لینک زیر هویت خود را تایید کنید حواستم جمع کن پنل گرونه
                            http://127.0.0.1:8000/acounts/api/V1/resend/{token}    
                                '''
        to=[serializer.validated_data["phone"]]
        Send_SMS(to, message)
        
        return Response({"detail": "SMS Resend for you..."})

    def get_tokens_for_user(self, user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)