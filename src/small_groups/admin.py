from django.contrib import admin

from small_groups.models import SmallGroup, GroupMember

admin.site.register(SmallGroup)
admin.site.register(GroupMember)
