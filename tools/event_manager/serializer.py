# coding: utf-8

from rest_framework import serializers
from .models import HolidayCalendar,UsageRecord,UserInformation,Room
from accounts.serializer import PublicHallSerializer
from common.serializer_lib import GetChoiceField
from common.serializer import UsageFeeSerializer

class HolidayCalendarSerializer(serializers.ModelSerializer):
	serializer_choice_field = GetChoiceField
	public_hall = PublicHallSerializer()
 
	class Meta:
		model = HolidayCalendar
		fields = '__all__'

class UserInformationSerializer(serializers.ModelSerializer):
	serializer_choice_field = GetChoiceField
	public_hall = PublicHallSerializer()
 
	class Meta:
		model = UserInformation
		fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
	serializer_choice_field = GetChoiceField
	public_hall = PublicHallSerializer()
	type = UsageFeeSerializer()
 
	class Meta:
		model = Room
		fields = '__all__'

class UsageRecordSerializer(serializers.ModelSerializer):
	serializer_choice_field = GetChoiceField
	public_hall = PublicHallSerializer()
	user = UserInformationSerializer()
	room1 = RoomSerializer()
 
	class Meta:
		model = UsageRecord
		fields = '__all__'
