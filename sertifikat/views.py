from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Sertifikat
from .serializers import SertifikatSerializer

class SertifikatViewSet(viewsets.ModelViewSet):
    queryset = Sertifikat.objects.all()
    serializer_class = SertifikatSerializer