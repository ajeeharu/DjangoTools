# coding: utf-8

from rest_framework import serializers
from .models import Creditor
from accounts.serializer import PublicHallSerializer

class CreditorSerializer(serializers.ModelSerializer):
	public_hall=PublicHallSerializer()
	class Meta:
		model = Creditor
		fields = '__all__'
