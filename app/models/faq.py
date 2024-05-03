from django.db import models


class Faq(models.Model):
    question = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    answer = models.CharField(max_length=2000)

    def __str__(self):
        return f'<Faq {self.question}>'