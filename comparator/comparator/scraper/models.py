from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=100)
    when = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
