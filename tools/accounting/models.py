from django.db import models
from accounts.models import PublicHall
import datetime

def GetCurrentYear():
	today=datetime.date.today()
	return today.year

# 債権者情報
class Creditor(models.Model):
	name = models.CharField('社名', max_length=64)
	address = models.CharField('住所', max_length=64)
	public_hall = models.ForeignKey(PublicHall,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

# 納入者情報
class Supplier(models.Model):
	name = models.CharField('社名', max_length=64)
	address = models.CharField('住所', max_length=64)
	public_hall = models.ForeignKey(PublicHall,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

# 会計年度情報
class FiscalTerms(models.Model):
	name = models.CharField('会計年度タイトル', max_length=32)
	start_month = models.SmallIntegerField('開始月')
	end_month = models.SmallIntegerField('終了月')

	def __str__(self):
		return self.name

# 出納帳
class AccountingBook(models.Model):
	name = models.CharField('出納帳', max_length=32)
	fiscal_terms = models.ForeignKey( FiscalTerms,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

# 科目（支出)
class SubjectSpending(models.Model):
	name = models.CharField('科目名', max_length=32)
	accounting_book = models.ManyToManyField(AccountingBook)
	acronym = models.CharField('略語',max_length=8)

	def __str__(self):
		return self.name

# 節（支出)
class SectionSpending(models.Model):
	FORMAT = (
			('0', '支出命令（様式１)'),
			('1', '支出命令（様式２)'),
			('2', '支出命令（様式３)')
	)
	name = models.CharField('節名', max_length=32)
	subject_spending = models.ManyToManyField(SubjectSpending)
	print_format = models.CharField('印刷FORMAT',max_length=2,choices=FORMAT,default='0')
	acronym = models.CharField('略語',max_length=8)

	def __str__(self):
		return self.name

# 予算（支出科目毎)
class BudgetSpending(models.Model):
	amount = models.IntegerField('予算額', default=0)
	subject_spending = models.ForeignKey(SubjectSpending, on_delete=models.CASCADE)
	year = models.SmallIntegerField('対象年度(西暦)',default=GetCurrentYear)
	public_hall = models.ForeignKey(PublicHall, on_delete=models.CASCADE)

# 科目（収入)
class SubjectIncome(models.Model):
	name = models.CharField('科目名', max_length=32)
	fiscal_terms = models.ManyToManyField(AccountingBook)
	acronym = models.CharField('略語',max_length=8)

	def __str__(self):
		return self.name

# 節（収入)
class SectionIncome(models.Model):
	FORMAT = (
			('0', '収入命令'),
	)
	name = models.CharField('節名', max_length=32)
	subject_income = models.ManyToManyField(SubjectIncome)
	print_format = models.CharField('印刷FORMAT',max_length=2,choices=FORMAT,default='0')
	acronym = models.CharField('略語',max_length=8)

	def __str__(self):
		return self.name

# 予算（収入科目毎)
class BudgetIncome(models.Model):
	amount = models.IntegerField('予算額', default=0)
	subject_income = models.ForeignKey(SubjectIncome, on_delete=models.CASCADE)
	year = models.SmallIntegerField('対象年度(西暦)',default=GetCurrentYear)
	public_hall = models.ForeignKey(PublicHall, on_delete=models.CASCADE)

# 支出詳細
class SpendingRecord(models.Model):
	number = models.IntegerField('支出番号')
	date = models.DateField('日付')
	accounting_book = models.ForeignKey(AccountingBook, on_delete=models.CASCADE)
	subject_spending = models.ForeignKey(SubjectSpending, on_delete=models.CASCADE)
	section_spending = models.ForeignKey(SectionSpending, on_delete=models.CASCADE)
	description = models.CharField('摘要', max_length=64)
	amount = models.IntegerField('金額', default=0)
	memo = models.CharField('メモ（印刷対象外)', max_length=64, blank=True)
	receipt = models.FileField(upload_to ='receipt/%Y/%m/%d/',null=True)
	estimate = models.FileField(upload_to ='estimate/%Y/%m/%d/',null=True)
	creditor = models.ForeignKey(Creditor, on_delete=models.CASCADE)
	behalf_pay = models.BooleanField('立替',default=False)
	rebersal_monies = models.BooleanField('戻入',default=False)
	tax_withholding = models.BooleanField('源泉',default=False)
	back_side = models.BooleanField('裏面',default=False)
	attachement = models.BooleanField('別紙',default=False)

	def __str__(self):
			return self.number+'：'+self.description

# 収入詳細
class IncomeRecord(models.Model):
	number = models.IntegerField('収入番号')
	date = models.DateField('日付')
	accounting_book = models.ForeignKey(AccountingBook, on_delete=models.CASCADE)
	subject_income = models.ForeignKey(SubjectIncome, on_delete=models.CASCADE)
	section_income = models.ForeignKey(SectionIncome, on_delete=models.CASCADE)
	description = models.CharField('摘要', max_length=64)
	amount = models.IntegerField('金額', default=0)
	memo = models.CharField('メモ（印刷対象外)', max_length=64, blank=True)
	receipt = models.FileField(upload_to ='receipt/%Y/%m/%d/',null=True)
	estimate = models.FileField(upload_to ='estimate/%Y/%m/%d/',null=True)
	creditor = models.ForeignKey(Supplier, on_delete=models.CASCADE)

	def __str__(self):
			return self.number+'：'+self.description
