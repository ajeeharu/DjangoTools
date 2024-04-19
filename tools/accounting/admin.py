from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Creditor,Supplier,FiscalTerms,AccountingBook,SubjectSpending,SectionSpending,BudgetSpending,SectionIncome,SubjectIncome,BudgetIncome,SpendingRecord,IncomeRecord

class CreditorAdmin(VersionAdmin):
	pass
admin.site.register(Creditor, CreditorAdmin)

class SupplierAdmin(VersionAdmin):
	pass
admin.site.register(Supplier, SupplierAdmin)

class FiscalTermsAdmin(VersionAdmin):
	pass
admin.site.register(FiscalTerms, FiscalTermsAdmin)

class AccountingBookAdmin(VersionAdmin):
	pass
admin.site.register(AccountingBook, AccountingBookAdmin)

class SubjectSpendingAdmin(VersionAdmin):
	pass
admin.site.register(SubjectSpending, SubjectSpendingAdmin)

class SectionSpendingAdmin(VersionAdmin):
	pass
admin.site.register(SectionSpending, SectionSpendingAdmin)

class BudgetSpendingAdmin(VersionAdmin):
	pass
admin.site.register(BudgetSpending, BudgetSpendingAdmin)

class SectionIncomeAdmin(VersionAdmin):
	pass
admin.site.register(SectionIncome, SectionIncomeAdmin)

class SubjectIncomeAdmin(VersionAdmin):
	pass
admin.site.register(SubjectIncome, SubjectIncomeAdmin)

class BudgetIncomeAdmin(VersionAdmin):
	pass
admin.site.register(BudgetIncome, BudgetIncomeAdmin)

class SpendingRecordAdmin(VersionAdmin):
	pass
admin.site.register(SpendingRecord, SpendingRecordAdmin)

class IncomeRecordAdmin(VersionAdmin):
	pass
admin.site.register(IncomeRecord, IncomeRecordAdmin)
