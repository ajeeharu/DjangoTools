from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import UsageFee,RegularHoliday

class UsageFeeAdmin(VersionAdmin):
    pass

admin.site.register(UsageFee, UsageFeeAdmin)

class RegularHolidayAdmin(VersionAdmin):
    pass

admin.site.register(RegularHoliday, RegularHolidayAdmin)
# Register your models here.
