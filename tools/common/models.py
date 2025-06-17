from django.db import models

SEMIWEEK_CHOICES = (
    ('0','指定なし'),
    ('1','毎週曜日'),
    ('2','第１曜日・第３曜日'),
    ('3','第２曜日・第４曜日'),
    ('4','第１曜日'),
    ('5','第２曜日'),    
    ('6','第３曜日'),
    ('7','第４曜日'),   
)
DAY_OF_WEEK_CHOICES = (
    ('0','指定なし'),
    ('1','月曜日'),
    ('2','火曜日'),
    ('3','水曜日'),
    ('4','木曜日'),
    ('5','金曜日'),    
    ('6','土曜日'),
    ('7','日曜日'), 
)

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

class RegularHoliday(models.Model):
	day_of_week = models.CharField('曜日指定',max_length=2,choices=DAY_OF_WEEK_CHOICES,default='0')
	semiweekly = models.CharField('隔週指定',max_length=2,choices=SEMIWEEK_CHOICES,default='0')

	def __str__(self):
		return '休館日'+self.get_semiweekly_display()+':'+self.get_day_of_week_display()

