from django.db import models


class Track(models.Model):
    tracking_number = models.BigIntegerField()
    from_target = models.CharField(max_length=255)
    to_target = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    from_longitude = models.FloatField()
    from_latitude = models.FloatField()

    to_longitude = models.FloatField()
    to_latitude = models.FloatField()

    def __str__(self):
        return f'<Track {self.tracking_number}>'