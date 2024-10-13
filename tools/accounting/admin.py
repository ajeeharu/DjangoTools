from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Creditor,Supplier,AccountingBook,SubjectSpending,SectionSpending,SectionIncome,SubjectIncome,SpendingRecord,IncomeRecord,PageManager,FiscalTerms

class CreditorAdmin(VersionAdmin):
	pass
admin.site.register(Creditor, CreditorAdmin)

class SupplierAdmin(VersionAdmin):
	pass
admin.site.register(Supplier, SupplierAdmin)

class AccountingBookAdmin(VersionAdmin):
	pass
admin.site.register(AccountingBook, AccountingBookAdmin)

class SubjectSpendingAdmin(VersionAdmin):
	pass
admin.site.register(SubjectSpending, SubjectSpendingAdmin)

class SectionSpendingAdmin(VersionAdmin):
	pass
admin.site.register(SectionSpending, SectionSpendingAdmin)

class SectionIncomeAdmin(VersionAdmin):
	pass
admin.site.register(SectionIncome, SectionIncomeAdmin)

class SubjectIncomeAdmin(VersionAdmin):
	pass
admin.site.register(SubjectIncome, SubjectIncomeAdmin)

class SpendingRecordAdmin(VersionAdmin):
	pass
admin.site.register(SpendingRecord, SpendingRecordAdmin)

class IncomeRecordAdmin(VersionAdmin):
	pass
admin.site.register(IncomeRecord, IncomeRecordAdmin)

class PageManagerAdmin(VersionAdmin):
	list_display = ("id", "number")
admin.site.register(PageManager, PageManagerAdmin)

class FiscalTermsAdmin(VersionAdmin):
	pass
admin.site.register(FiscalTerms, FiscalTermsAdmin)
