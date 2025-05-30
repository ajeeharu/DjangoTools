from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import Room,UserInformation,UsageRecord

class RoomAdmin(VersionAdmin):
	pass
admin.site.register(Room, RoomAdmin)

class UserInformationAdmin(VersionAdmin):
	pass
admin.site.register(UserInformation, UserInformationAdmin)

class UsageRecordAdmin(VersionAdmin):
	pass
admin.site.register(UsageRecord, UsageRecordAdmin)

# Register your models here.
