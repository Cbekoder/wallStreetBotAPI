from email.headerregistry import Group

from django.contrib import admin
from .models import Channels
from django.contrib.auth.models import Group, User


admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(Channels)
class ChannelsAdmin(admin.ModelAdmin):
    list_display = ('name', 'chat_id')
    list_display_links = ('name', 'chat_id')


