import traceback

from django.contrib.auth import logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import UserRegisterSerializer


class RegistrationView(APIView):
    """

    """
    permission_classes = []
    authentication_classes = []

    def post(self, *args, **kwargs):
        try:
            serializer = UserRegisterSerializer(data=self.request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(traceback.format_exc())  # for error_log
            return Response(data=str(ex), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LogoutView(APIView):
    """

    """

    def post(self, *args, **kwargs):
        logout(self.request)
        return Response(True, status=status.HTTP_200_OK)


class AboutMeView(APIView):
    """

    """

    def get(self, *args, **kwargs):
        return Response({"username": "test", "email": "bcolak@gmail.com"}, status=status.HTTP_200_OK)
