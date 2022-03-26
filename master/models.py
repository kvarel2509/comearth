from django.db import models


class Pattern(models.Model):
    string = models.TextField('Исходная строка')
    prepared = models.JSONField('Заготовка')
    count_variable = models.IntegerField('Количество переменных')
