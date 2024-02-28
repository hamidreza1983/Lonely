from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from acounts.api.V1.serializers import RegisterationSerializer


class RegistrationView(GenericAPIView):
    '''this class is for register users'''
    serializer_class = RegisterationSerializer

    def post(self, request, *args, **kwargs):
        '''this function validate and create a user'''
        serializer = RegisterationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.validated_data)
            data = {"email": serializer.validated_data["email"]}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
