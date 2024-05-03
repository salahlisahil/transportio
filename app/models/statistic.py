from django.db import models


class Statistic(models.Model):
    name = models.CharField(max_length=255)
    value = models.BigIntegerField()
    main_page = models.BooleanField()

    def __str__(self):
        return f'<Statistic {self.name}>'