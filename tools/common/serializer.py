# coding: utf-8

from rest_framework import serializers
from .models import RegularHoliday, UsageFee
from accounts.serializer import PublicHallSerializer
from common.serializer_lib import GetChoiceField


class RegularHolidaySerializer(serializers.ModelSerializer):
    serializer_choice_field = GetChoiceField

    class Meta:
        model = RegularHoliday
        fields = '__all__'


class UsageFeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsageFee
        fields = '__all__'
