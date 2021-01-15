import traceback

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from authentication.serializers import GenericModelSerializer


class RegistrationView(APIView):
    """

    """
    permission_classes = []
    authentication_classes = []

    def post(self, *args, **kwargs):
        try:
            serializer = GenericModelSerializer(data=self.request.data, model=User, exclude=('id', 'password'))
            if serializer.is_valid():
                User.objects.create_user(**serializer.validated_data)
                return Response(status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(traceback.format_exc())  # for error_log
            return Response(data=str(ex), status=status.HTTP_500_INTERNAL_SERVER_ERROR)