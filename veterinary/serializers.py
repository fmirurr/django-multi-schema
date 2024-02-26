from rest_framework.serializers import ModelSerializer

from veterinary.models import Veterinary


class VeterinaryModelSerializer(ModelSerializer):
    class Meta:
        model = Veterinary
        fields = ('name',)
