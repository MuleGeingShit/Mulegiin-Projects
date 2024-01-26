from django.db import models

# Create your models here.

class card(models.Model):
    img = models.CharField(max_length = 255)
    title = models.TextField()
    body = models.TextField()
    def __str__(self):
        return self.name