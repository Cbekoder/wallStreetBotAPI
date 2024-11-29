from django.contrib import admin
from .models import Members


@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ('id', 'telegram_id', 'first_name', 'username', 'phone_number', 'created_at')
    search_fields = ('telegram_id', 'first_name','username', 'phone_number')
    list_filter = ('created_at',)
    fields = ('telegram_id', 'first_name', 'username', 'phone_number', 'created_at')
    readonly_fields = ('created_at',)
