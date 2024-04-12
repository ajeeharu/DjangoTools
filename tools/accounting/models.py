from django.db import models

# 公民館情報
# class PublicHall(models.Model):
# 	number = models.DecimalField('公民館No.',primary_key=True, unique=True,max_digits=3, decimal_places=0)
# 	name = models.CharField('公民館名', max_length=64)
# 	email = models.EmailField('メールアドレス', max_length=100)
# 	tel = models.CharField('電話番号', max_length=16)

# 	def __str__(self):
# 		return self.name