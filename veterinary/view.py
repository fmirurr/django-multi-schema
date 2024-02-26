from rest_framework import status
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated

from veterinary.serializers import VeterinaryModelSerializer


class Veterinary_ViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = VeterinaryModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        veterinary = serializer.save()
        data = VeterinaryModelSerializer(veterinary).data
        return Response(data, status=status.HTTP_201_CREATED)
