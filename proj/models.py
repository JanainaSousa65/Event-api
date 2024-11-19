from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return self.name
# Create your models here.
