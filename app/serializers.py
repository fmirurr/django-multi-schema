from rest_framework import serializers

from .models import Client, Domain


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'schema_name', 'name', 'paid_until', 'on_trial')


class DomainSerializers(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ('id', 'domain', 'tenant_id', 'is_primary')
