from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from mail_templated import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken
from acounts.api.V1.serializer import (
    ResendEmailSerializer,
)              
from acounts.multi_threading import SendEmailWithThreading

class ResendEmailView(GenericAPIView):
    '''Resend Email  to user  for verification '''
    serializer_class = ResendEmailSerializer

    def post(self, request, *args, **kwargs):
        ''' This method is used to resend email to user  for verification '''
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        if user.is_verified:
            return Response({"detail": "your email is already verified"})
        token = self.get_tokens_for_user(user)
        message = EmailMessage(
            "email/email.html",
            {"token": token},
            "negim@gmail.com",
            to=[serializer.validated_data["email"]],
        )
        email = SendEmailWithThreading(message)
        email.start()
        return Response({"detail": "email Resend for you..."})

    def get_tokens_for_user(self, user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)