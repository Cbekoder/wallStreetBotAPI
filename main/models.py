from django.db import models

class Channels(models.Model):
    name = models.CharField(max_length=50, null=True, blank=False, verbose_name="Channel Name")
    chat_id = models.CharField(max_length=50, unique=True, null=True, blank=False, verbose_name="Channel ID")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Channel"
        verbose_name_plural = "Channels"


