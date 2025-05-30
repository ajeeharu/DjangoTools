from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import HolidayCalendar,UsageFee

class HolidayCalendarAdmin(VersionAdmin):
	pass

admin.site.register(HolidayCalendar, HolidayCalendarAdmin)

class UsageFeeAdmin(VersionAdmin):
    pass

admin.site.register(UsageFee, UsageFeeAdmin)
# Register your models here.
