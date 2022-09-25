from django.db import models
class Try(models.Model):
    Name=models.CharField(max_length=30)
    def __str__(self):
        return self.Name
# Create your models here.
