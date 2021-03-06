from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.CharField(max_length=255)
    url = models.TextField()

    def __str__(self):
        return self.title