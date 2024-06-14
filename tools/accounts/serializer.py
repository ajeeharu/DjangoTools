# coding: utf-8

from rest_framework import serializers
from .models import PublicHall

class PublicHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicHall
        fields = '__all__'
