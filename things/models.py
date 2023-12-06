from django.db import models

class Things(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.TextField(max_length=120, blank=True)
    quantity = models.IntegerField(default=0, choices=[(i, i) for i in range(101)])
