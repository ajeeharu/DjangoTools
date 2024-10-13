# coding: utf-8

from rest_framework import serializers
from .models import Creditor,Supplier,FiscalTerms,AccountingBook,SubjectSpending,SectionSpending,SubjectIncome,SectionIncome,PageManager,SpendingRecord,IncomeRecord
from accounts.serializer import PublicHallSerializer
from common.serializer_lib import GetChoiceField

class CreditorSerializer(serializers.ModelSerializer):
	public_hall=PublicHallSerializer()

	class Meta:
		model = Creditor
		fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
	public_hall=PublicHallSerializer()

	class Meta:
		model = Supplier
		fields = '__all__'

class FiscalTermsSerializer(serializers.ModelSerializer):
	class Meta:
		model = FiscalTerms
		fields = '__all__'

class AccountingBookSerializer(serializers.ModelSerializer):
	class Meta:
		model = AccountingBook
		fields = '__all__'

class SubjectSpendingSerializer(serializers.ModelSerializer):
	public_hall=PublicHallSerializer()

	class Meta:
		model = SubjectSpending
		fields = '__all__'

class SectionSpendingSerializer(serializers.ModelSerializer):
	serializer_choice_field = GetChoiceField

	class Meta:
		model = SectionSpending
		fields = '__all__'

class SubjectIncomeSerializer(serializers.ModelSerializer):
	public_hall=PublicHallSerializer()

	class Meta:
		model = SubjectIncome
		fields = '__all__'

class SectionIncomeSerializer(serializers.ModelSerializer):
	serializer_choice_field = GetChoiceField

	class Meta:
		model = SectionIncome
		fields = '__all__'

class SpendingRecordSerializer(serializers.ModelSerializer):
	subject_spending = SubjectSpendingSerializer()
	section_spending = SectionSpendingSerializer()
	creditor = CreditorSerializer()

	class Meta:
		model = SpendingRecord
		fields = '__all__'

class IncomeRecordSerializer(serializers.ModelSerializer):
	subject_income = SubjectIncomeSerializer()
	section_income = SectionIncomeSerializer()
	supplier = SupplierSerializer()

	class Meta:
		model = IncomeRecord
		fields = '__all__'

class PageManagerSerializer(serializers.ModelSerializer):
	serializer_choice_field = GetChoiceField
	spending_record = SpendingRecordSerializer()
	income_record = IncomeRecordSerializer()

	class Meta:
		model = PageManager
		fields = '__all__'
