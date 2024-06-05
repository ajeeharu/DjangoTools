from django.db import models
from django.contrib.auth.models import (BaseUserManager,
                                        AbstractBaseUser,
                                        PermissionsMixin)
from django.utils.translation import gettext_lazy as _


# 公民館情報
class PublicHall(models.Model):
	number = models.DecimalField('公民館No.',primary_key=True, unique=True,max_digits=4, decimal_places=0)
	name = models.CharField('公民館名', max_length=32)
	email = models.EmailField('メールアドレス', max_length=128)
	tel = models.CharField('電話番号', max_length=16)
	director = models.CharField('館長', max_length=32)

	def __str__(self):
		return self.name

class UserManager(BaseUserManager):
    def _create_user(self, email, login_user, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, login_user=login_user, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, login_user, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email=email,
            login_user=login_user,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, email, login_user, password, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(
            email=email,
            login_user=login_user,
            password=password,
            **extra_fields,
        )


class User(AbstractBaseUser, PermissionsMixin):

    login_user = models.CharField(
        verbose_name=_("login user"),
        unique=True,
        max_length=64,
    )
    email = models.EmailField(
        verbose_name=_("email"),
        # unique=True
    )
    name = models.CharField(
        verbose_name=_("name"),
        max_length=150,
        null=True,
        blank=False
    )
    public_hall = models.ForeignKey(
         PublicHall,
         on_delete=models.CASCADE,
         null=True,
         blank=True,
    )

    is_superuser = models.BooleanField(
        verbose_name=_("is_superuer"),
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name=_('staff status'),
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created_at"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updateded_at"),
        auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'login_user' # ログイン時、ユーザー名の代わりにlogin_userを使用
    REQUIRED_FIELDS = ['email']  # スーパーユーザー作成時にemailも設定する

    def __str__(self):
        return self.login_user





