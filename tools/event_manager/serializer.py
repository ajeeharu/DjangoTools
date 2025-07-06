# coding: utf-8

from rest_framework import serializers
from .models import HolidayCalendar,UsageRecord,UserInformation
from accounts.serializer import PublicHallSerializer
from common.serializer_lib import GetChoiceField

class HolidayCalendarSerializer(serializers.ModelSerializer):
	serializer_choice_field = GetChoiceField
	public_hall = PublicHallSerializer()
 
	class Meta:
		model = HolidayCalendar
		fields = '__all__'

class UsageRecordSerializer(serializers.ModelSerializer):
	serializer_choice_field = GetChoiceField
	public_hall = PublicHallSerializer()
 
	class Meta:
		model = UsageRecord
		fields = '__all__'

class UserInformationSerializer(serializers.ModelSerializer):
	serializer_choice_field = GetChoiceField
	public_hall = PublicHallSerializer()
 
	class Meta:
		model = UserInformation
		fields = '__all__'