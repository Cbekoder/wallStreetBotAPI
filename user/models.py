from django.db import models

from quiz.models import Level


class Members(models.Model):
    telegram_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30, null=True,  blank=False)
    username = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class MemberResults(models.Model):
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    questions = models.JSONField()
    score = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'User Result'
        verbose_name_plural = 'User Results'