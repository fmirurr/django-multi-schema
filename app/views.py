from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Client, Domain

from .serializers import ClientSerializers, DomainSerializers


# Create your views here.
class App_ApiView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        client = Client.objects.all()
        serializer = ClientSerializers(client, many=True)
        return Response(serializer.data)

    def post(self, request):
        data_client = request.data["client"]
        tenant = Client(schema_name=data_client["schema_name"],
                        name=data_client["name"], paid_until=data_client["paid_until"], on_trial=True)
        tenant.save()
        data_domain = request.data["domain"]
        domain = Domain(
            domain=data_domain["domain"], tenant=tenant, is_primary=True)
        domain.save()
        data = {'tenant': tenant.schema_name, 'domain': domain.domain}
        return Response(data, status=status.HTTP_201_CREATED)
