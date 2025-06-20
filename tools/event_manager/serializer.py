# coding: utf-8

from rest_framework import serializers
from .models import HolidayCalendar
from accounts.serializer import PublicHallSerializer
from common.serializer_lib import GetChoiceField

class HolidayCalendarSerializer(serializers.ModelSerializer):
	serializer_choice_field = GetChoiceField
	public_hall = PublicHallSerializer()
 
	class Meta:
		model = HolidayCalendar
		fields = '__all__'
