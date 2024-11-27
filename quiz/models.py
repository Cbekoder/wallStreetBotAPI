from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='levels/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Level'
        verbose_name_plural = 'Levels'

class Question(models.Model):
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=False)
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'


