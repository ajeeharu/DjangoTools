from django.contrib import admin
from django.contrib.auth.models import Group

from .models import PublicHall,User

class PublicHallAdmin(admin.ModelAdmin):
    list_display = ("name", "number") # 公民館名と公民館No.を表示

admin.site.register(PublicHall, PublicHallAdmin)

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)  # Groupモデルは不要のため非表示にします