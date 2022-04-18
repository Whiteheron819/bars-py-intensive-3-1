from django.db import models


class Worker(models.Model):
    first_name = models.CharField('Имя', max_length=200)
    last_name = models.CharField('Фамилия', max_length=200)

    def __str__(self):
        return self.first_name + self.last_name

    class Meta:
        db_table = 'worker'
