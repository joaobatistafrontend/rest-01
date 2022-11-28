from rest_framework import routers, serializers, viewsets
from .models import Cliente



class CientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id','nome','endereco','idade')