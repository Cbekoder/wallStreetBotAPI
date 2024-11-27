from django.db import models

class Members(models.Model):
    telegram_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=False)
    last_name = models.CharField(max_length=30, null=True, blank=False)
    username = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=False)
    studying_time = models.CharField(max_length=50, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.telegram_id

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
