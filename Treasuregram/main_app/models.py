from django.db import models
from django.contrib.auth.models import User

class Treasure(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING, null=False)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10,decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

