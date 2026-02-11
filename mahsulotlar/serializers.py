# serializers.py
from rest_framework import serializers
from .models import Mahsulot

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'