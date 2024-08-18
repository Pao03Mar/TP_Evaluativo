from django.db import models

# Create your models here.
class TuModelo(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()
    is_deleted = models.BooleanField(default=False)