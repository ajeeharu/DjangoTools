from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Room,UserInformation,UsageRecord,HolidayCalendar
class RoomAdmin(VersionAdmin):
	pass
admin.site.register(Room, RoomAdmin)

class UserInformationAdmin(VersionAdmin):
	pass
admin.site.register(UserInformation, UserInformationAdmin)

class UsageRecordAdmin(VersionAdmin):
	pass
admin.site.register(UsageRecord, UsageRecordAdmin)

class HolidayCalendarAdmin(VersionAdmin):
	pass
admin.site.register(HolidayCalendar, HolidayCalendarAdmin)

# Register your models here.
