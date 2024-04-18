from django.contrib import admin
from .models import Creditor,Supplier,FiscalTerms,AccountingBook,SubjectSpending,SectionSpending,BudgetSpending,SectionIncome,SubjectIncome,BudgetIncome,SpendingRecord,IncomeRecord

class CreditorAdmin(admin.ModelAdmin):
	pass
admin.site.register(Creditor, CreditorAdmin)

class SupplierAdmin(admin.ModelAdmin):
	pass
admin.site.register(Supplier, SupplierAdmin)

class FiscalTermsAdmin(admin.ModelAdmin):
	pass
admin.site.register(FiscalTerms, FiscalTermsAdmin)

class AccountingBookAdmin(admin.ModelAdmin):
	pass
admin.site.register(AccountingBook, AccountingBookAdmin)

class SubjectSpendingAdmin(admin.ModelAdmin):
	pass
admin.site.register(SubjectSpending, SubjectSpendingAdmin)

class SectionSpendingAdmin(admin.ModelAdmin):
	pass
admin.site.register(SectionSpending, SectionSpendingAdmin)

class BudgetSpendingAdmin(admin.ModelAdmin):
	pass
admin.site.register(BudgetSpending, BudgetSpendingAdmin)

class SectionIncomeAdmin(admin.ModelAdmin):
	pass
admin.site.register(SectionIncome, SectionIncomeAdmin)

class SubjectIncomeAdmin(admin.ModelAdmin):
	pass
admin.site.register(SubjectIncome, SubjectIncomeAdmin)

class BudgetIncomeAdmin(admin.ModelAdmin):
	pass
admin.site.register(BudgetIncome, BudgetIncomeAdmin)

class SpendingRecordAdmin(admin.ModelAdmin):
	pass
admin.site.register(SpendingRecord, SpendingRecordAdmin)

class IncomeRecordAdmin(admin.ModelAdmin):
	pass
admin.site.register(IncomeRecord, IncomeRecordAdmin)
