from django.db import models
from django.forms import widgets

# Create your models here.


class Pull(models.Model):
    survey = models.CharField(max_length=20, null=False, blank=False, verbose_name='Survey')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Uploaded')

    def __str__(self):
        return f'{self.survey}'


class Choice(models.Model):
    option = models.CharField(max_length=100, null=False, blank=False, verbose_name='Option')
    pull = models.ForeignKey('webapp.Pull', related_name='pull', on_delete=models.CASCADE, verbose_name='Pull')

    def __str__(self):
        return f'{self.option}'


class Answer(models.Model):
    pull_fk = models.ForeignKey('webapp.Pull', related_name='pull_fk', on_delete=models.CASCADE, verbose_name='Pull')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Answered')
    option_fk = models.ForeignKey('webapp.Choice', related_name='option_fk', on_delete=models.CASCADE,
                                  verbose_name='Option')

    def __str__(self):
        return f'{self.option}'


