# coding: utf-8

from rest_framework import serializers
from .models import Creditor

class CreditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creditor
        fields = '__all__'
