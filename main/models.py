from django.db import models

class Channels(models.Model):
    pass

    def __str__(self):
        return "Channels"

    class Meta:
        verbose_name = "Channel"
        verbose_name_plural = "Channels"



class Channel(models.Model):
    channels = models.ForeignKey(Channels, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Channel Name")
    chat_id = models.CharField(max_length=50, unique=True, verbose_name="Channel ID")

    def __str__(self):
        return self.chat_id