from django.shortcuts import render
from .serializers import CientesSerializer
from .models import Cliente
from rest_framework import viewsets


class CleinteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = CientesSerializer