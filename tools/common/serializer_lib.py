# coding: utf-8

from rest_framework import serializers

# Choices テーブル用変換関数
class GetChoiceField(serializers.ChoiceField):
	def to_representation(self, obj):
			choice = getattr(self, '_choices')
			key = str(obj)
			if key in choice:
				return {'key': key, 'value': choice[key]}
			else:
				return {'key': key, 'value': ''}
