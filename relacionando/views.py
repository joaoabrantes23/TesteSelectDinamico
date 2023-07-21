from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Ods, Unidade, Cronograma
from .serializers import OdsSerializer, UnidadeSerializer, CronogramaSerializer

class OdsViewSet(viewsets.ModelViewSet):
    queryset = Ods.objects.all()
    serializer_class = OdsSerializer

class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

class CronogramaViewSet(viewsets.ModelViewSet):
    queryset = Cronograma.objects.all()
    serializer_class = CronogramaSerializer