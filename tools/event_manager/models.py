from django.db import models
from accounts.models import PublicHall,User
from common.models import UsageFee,SEMIWEEK_CHOICES,DAY_OF_WEEK_CHOICES

# Create your models here.
EDUCATION_PROGRAM_CHOICES = (
    ('X','指定なし'),
    ('0','家庭教育事業'),
    ('1','少年教育事業'),
    ('2','青年教育事業'),
    ('3','福井学事業'),
    ('4','健康長寿事業'),
    ('5','男女共同参画促進事業'),
    ('6','多文化共生促進事業'),
    ('7','環境教育事業'),
    ('8','防犯防災教育事業'),
    ('9','人材育成事業'),
    ('A','市民ICT事業'),
    ('B','地域ICT事業'),
    ('C','伝統文化伝承事業'),
    ('D','その他の地域課題解決事業'),
)
USAGE_CATEGORY_CHOICES = (
    ('0','教育事業'),
    ('1','公民館企画の事業・会議・研修'),
    ('2','自主グループ'),
    ('3','公民館が他の団体と共催する事業'),
    ('4','団体が開催する事業・会議'),
    ('5','その他の事務事業'), 
    ('X','休館日'),
    ('Z','配布日'),
)

USAGE_FEE_CHOICES = (
    ('0','有'),
    ('1','無（社会教育）'),
    ('2','無（公共福祉）'),
    ('3','無（市長許可）'),
)
# 利用施設データ
class Room(models.Model):
	name = models.CharField('利用施設名', max_length=64, blank=False)
	type = models.ForeignKey(UsageFee, null=True,on_delete=models.CASCADE)

	public_hall = models.ForeignKey(PublicHall,on_delete=models.CASCADE)

	def __str__(self):
		return self.name


# 利用者データ
class UserInformation(models.Model):
	organization_name = models.CharField('使用団体名', max_length=64, blank=False)
	usage_category = models.CharField('使用区分',max_length=2,choices=USAGE_CATEGORY_CHOICES,blank=False)
	educational_category = models.CharField('教育事業区分',max_length=2,choices=EDUCATION_PROGRAM_CHOICES,blank=True,default='X')
	day_of_week = models.CharField('曜日指定',max_length=2,choices=DAY_OF_WEEK_CHOICES,default='X')
	semiweekly = models.CharField('隔週指定',max_length=2,choices=SEMIWEEK_CHOICES,default='X')
	responsible_party = models.CharField('責任者', max_length=64,blank=True)
	address = models.CharField('住所', max_length=64,blank=True)
	tel = models.CharField('電話番号', max_length=16,blank=True)
	default_start_time = models.TimeField('開始時間（初期値）', null=True)
	default_end_time = models.TimeField('終了時間（初期値）', null=True)
	default_room = models.ForeignKey(Room, null=True,on_delete=models.CASCADE)
	default_remarks = models.CharField('備考（初期値）', max_length=128, blank=True)
	default_details = models.CharField('利用内容（初期値）', max_length=128, blank=True)

	public_hall = models.ForeignKey(PublicHall,on_delete=models.CASCADE)

	def __str__(self):
		return self.organization_name

# 利用実績データ
class UsageRecord(models.Model):
	number = models.IntegerField('受付番号', null=True)
	user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
	details = models.CharField('利用内容', max_length=128, blank=True)
	application_date = models.DateField('申請日', null=False)
	date_of_use = models.DateField('利用日', null=False)
	start_time = models.TimeField('開始時間', null=False)
	end_time = models.TimeField('終了時間', null=False)
	number_of_users = models.DecimalField('利用人数',max_digits=4,decimal_places=0)
	room1 = models.ForeignKey(Room,related_name='施設１',on_delete=models.CASCADE,null=False)
	room2 = models.ForeignKey(Room,related_name='施設２',on_delete=models.CASCADE,null=True)
	room3 = models.ForeignKey(Room,related_name='施設３',on_delete=models.CASCADE,null=True)
	air_conditioning = models.BooleanField('冷暖房',default=False)
	usage_fee_collection = models.CharField('使用料徴収',max_length=2,choices=USAGE_FEE_CHOICES,blank=False)
	remarks = models.CharField('備考・講師', max_length=128, blank=True)
	reception = models.ForeignKey(User, null=False,on_delete=models.CASCADE)
  
	public_hall = models.ForeignKey(PublicHall,on_delete=models.CASCADE)

	def __str__(self):
		return self.date_of_use+ '('+self.user+')'

# 常駐Event
class ParmanentEvent(models.Model):
	event = models.ForeignKey(UserInformation,on_delete=models.CASCADE)
	color = models.CharField('文字色', max_length=8, db_default="#ffffff")
	background_color = models.CharField('背景色', max_length=8, db_default="#0000cc")

	public_hall = models.ForeignKey(PublicHall,on_delete=models.CASCADE)

	def __str__(self):
		return self.event.organization_name

# 祝日カレンダー
class HolidayCalendar(models.Model):
    # https://holidays-jp.github.io/api/v1/2017/date.json から取得予定
	name = models.CharField('祝日名', max_length=32,blank=False)
	date = models.DateField('日付', null=False)

	public_hall = models.ForeignKey(PublicHall,on_delete=models.CASCADE)

	def __str__(self):
		return self.name


# https://qiita.com/imp555sti/items/ee9809768f6dc9439ab5
# https://vkurko.github.io/calendar/