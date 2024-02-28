from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from acounts.api.V1.serializer import PasswordChangeSerializer


class ChangePasswordView(GenericAPIView):
    '''
    we wrote this class for change user password
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = PasswordChangeSerializer

    def post(self, request, *args, **kwargs):
        '''this functions use for check old password and set new password'''
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.check_old_password(request, serializer.validated_data)
        serializer.set_new_password(request, serializer.validated_data)
        token = serializer.create_new_token(
            request, serializer.validated_data
        )

        return Response(
            data={
                "detail": "password change successfully.",
                "token": token.key,
            },
            status=status.HTTP_200_OK,
        )