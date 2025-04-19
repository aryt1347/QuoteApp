from django.db import models


class QuotesModel(models.Model):

    content = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    topic = models.CharField(max_length=25)
