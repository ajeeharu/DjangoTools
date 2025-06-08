from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import UsageFee

class UsageFeeAdmin(VersionAdmin):
    pass

admin.site.register(UsageFee, UsageFeeAdmin)
# Register your models here.
