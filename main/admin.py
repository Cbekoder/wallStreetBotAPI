from django.contrib import admin
from .models import Channels, Channel

class ChannelInline(admin.TabularInline):
    model = Channel
    extra = 0
    max_num = 5
    verbose_name = "Channel"
    verbose_name_plural = "Channels"

@admin.register(Channels)
class ChannelsAdmin(admin.ModelAdmin):
    inlines = [ChannelInline]

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False
