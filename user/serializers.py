from rest_framework import serializers
from .models import MemberResults, Members

class MemberRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['id', 'telegram_id', 'first_name', 'username', 'phone_number', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_telegram_id(self, value):
        if Members.objects.filter(telegram_id=value).exists():
            raise serializers.ValidationError("A user with this Telegram ID already exists.")
        return value



class MemberResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberResults
        fields = ['id', 'member', 'level', 'amount', 'score', 'created_at']
        read_only_fields = ['id', 'created_at']
