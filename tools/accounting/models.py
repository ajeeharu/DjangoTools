from django.db import models
from accounts.models import PublicHall
import datetime

def GetCurrentYear():
	today=datetime.date.today()
	return today.year

# 債権者情報
class Creditor(models.Model):
	name = models.CharField('社名', max_length=64,blank=False)
	address = models.CharField('住所', max_length=64,blank=False)
	public_hall = models.ForeignKey(PublicHall,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

# 納入者情報
class Supplier(models.Model):
	name = models.CharField('社名', max_length=64,blank=False)
	address = models.CharField('住所', max_length=64,blank=False)
	public_hall = models.ForeignKey(PublicHall,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

# 会計年度
class FiscalTerms(models.Model):
	name = models.CharField('会計年度名',max_length=32,blank=False)
	start_date = models.DateField('開始年月日',null=False)
	end_date = models.DateField('終了年月日',null=False)

	def __str__(self):
		return self.name


# 出納帳
class AccountingBook(models.Model):
	name = models.CharField('出納帳', max_length=32,blank=False)

	def __str__(self):
		return self.name


# 科目（支出)
class SubjectSpending(models.Model):
	name = models.CharField('科目名', max_length=32,blank=False)
	acronym = models.CharField('略語',max_length=8)
	budget = models.IntegerField('予算額')
	fiscal_terms = models.ForeignKey(FiscalTerms, on_delete=models.CASCADE,null=False)
	accountig_book = models.ForeignKey(AccountingBook, on_delete=models.CASCADE,null=False)
	public_hall = models.ForeignKey(PublicHall, on_delete=models.CASCADE,null=False)

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
	print_format = models.CharField('印刷FORMAT',max_length=2,choices=FORMAT,default='0')
	acronym = models.CharField('略語',max_length=8)

	def __str__(self):
		return self.name


# 科目（収入)
class SubjectIncome(models.Model):
	name = models.CharField('科目名', max_length=32,blank=False)
	acronym = models.CharField('略語',max_length=8)
	budget = models.IntegerField('予算額')
	fiscal_terms = models.ForeignKey(FiscalTerms, on_delete=models.CASCADE,null=False)
	accountig_book = models.ForeignKey(AccountingBook, on_delete=models.CASCADE,null=False)
	public_hall = models.ForeignKey(PublicHall, on_delete=models.CASCADE,null=False)

	def __str__(self):
		return self.name


# 節（収入)
class SectionIncome(models.Model):
	FORMAT = (
			('0', '収入命令'),
	)
	name = models.CharField('節名', max_length=32)
	print_format = models.CharField('印刷FORMAT',max_length=2,choices=FORMAT,default='0')
	acronym = models.CharField('略語',max_length=8)

	def __str__(self):
		return self.name


# 支出詳細
class SpendingRecord(models.Model):
	number = models.IntegerField('支出番号')
	date = models.DateField('日付')
	subject_spending = models.ForeignKey(SubjectSpending, on_delete=models.CASCADE,null=False)	# 支出科目
	section_spending = models.ForeignKey(SectionSpending, on_delete=models.CASCADE,null=False)	# 支出節
	description = models.CharField('摘要', max_length=64)
	amount = models.IntegerField('金額', default=0)
	memo = models.CharField('メモ（印刷対象外)', max_length=64, blank=True)
	receipt = models.FileField(upload_to ='receipt/%Y/%m/%d/',null=True) 			# 領収書
	estimate = models.FileField(upload_to ='estimate/%Y/%m/%d/',null=True) 		# 見積書等
	creditor = models.ForeignKey(Creditor, on_delete=models.CASCADE)					# 債権者
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
	subject_income = models.ForeignKey(SubjectIncome, on_delete=models.CASCADE,null=False)		# 収入科目
	section_income = models.ForeignKey(SectionIncome, on_delete=models.CASCADE,null=False)		# 収入節
	description = models.CharField('摘要', max_length=64)
	amount = models.IntegerField('金額', default=0)
	memo = models.CharField('メモ（印刷対象外)', max_length=64, blank=True)
	receipt = models.FileField(upload_to ='receipt/%Y/%m/%d/',null=True)
	estimate = models.FileField(upload_to ='estimate/%Y/%m/%d/',null=True)
	creditor = models.ForeignKey(Supplier, on_delete=models.CASCADE)							# 納入者

	def __str__(self):
			return self.number+'：'+self.description

# 一覧画面制御用
class PageManager(models.Model):
	SELECT = (
			('0', '支出命令'),
			('1', '収入命令'),
	)
	number = models.IntegerField('シリアル番号')
	fixed_number = models.BooleanField('番号固定',default=False)
	income_select = models.CharField('収支指定',max_length=2,choices=SELECT,default='0')
	accountig_book = models.ForeignKey(AccountingBook, on_delete=models.CASCADE,null=False)
	fiscal_terms = models.ForeignKey(FiscalTerms, on_delete=models.CASCADE,null=False)
	subject_income = models.ForeignKey(SpendingRecord, on_delete=models.CASCADE)	# 支出レコード
	section_income = models.ForeignKey(IncomeRecord, on_delete=models.CASCADE)		# 収入レコード
	public_hall = models.ForeignKey(PublicHall, on_delete=models.CASCADE,null=False)

	def __str__(self):
			return self.number

