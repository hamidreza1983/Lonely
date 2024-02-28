from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from mail_templated import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken
from ....multi_threading import SendEmailWithThreading
from acounts.api.V1.serializer import RegisterationSerializer
from acounts.models import CustomeUser


class RegistrationView(GenericAPIView):
    """
    this class is for register users
    """

    serializer_class = RegisterationSerializer

    def post(self, request, *args, **kwargs):
        """
        this function validate and create a user
        """
        serializer = RegisterationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = get_object_or_404(
                CustomeUser, email=serializer.validated_data["email"]
            )
            token = self.get_tokens_for_user(user)
            message = EmailMessage(
                "email/email.html",
                {"token": token},
                "negin@gmail.com",
                to=[serializer.validated_data["email"]],
            )
            email = SendEmailWithThreading(message)
            email.start()
            return Response({"detail": "email sent for your verification...!"})

            # print (serializer.validated_data)
            # data = {
            #     'email': serializer.validated_data['email']
            # }
            # return Response(data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
