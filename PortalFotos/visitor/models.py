from django.db import models

# Create your models here.

class Media(models.Model):
    img = models.ImageField(null=True)
    allowed = models.BooleanField(default=False)
