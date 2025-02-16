from rest_framework import serializers
from .models import Sertifikat

class SertifikatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sertifikat
        fields = '__all__'