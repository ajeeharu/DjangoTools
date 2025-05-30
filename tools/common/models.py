from django.db import models


# Create your models here.

# 施設使用料金テーブル
class UsageFee(models.Model):
	type = models.CharField('施設種類', max_length=64, blank=False)
	time_fee_1 = models.DecimalField('使用料金（午前）',max_digits=8,decimal_places=0,null=False)
	time_fee_2 = models.DecimalField('使用料金（午後）',max_digits=8,decimal_places=0,null=False)
	time_fee_3 = models.DecimalField('使用料金（夜間）',max_digits=8,decimal_places=0,null=False)
	time_fee_1_with_air = models.DecimalField('使用料金（午前）冷暖房',max_digits=8,decimal_places=0,null=False)
	time_fee_2_with_air = models.DecimalField('使用料金（午後）冷暖房',max_digits=8,decimal_places=0,null=False)
	time_fee_3_with_air = models.DecimalField('使用料金（夜間）冷暖房',max_digits=8,decimal_places=0,null=False)


	def __str__(self):
		return self.type

# 祝日カレンダー
class HolidayCalendar(models.Model):
    # https://holidays-jp.github.io/api/v1/2017/date.json から取得予定
	name = models.CharField('祝日名', max_length=32,blank=False)
	date = models.DateField('日付', null=False)

	def __str__(self):
		return self.name


