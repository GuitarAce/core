from django.db import models

# Create your models here.

class ClassPj(models.Model):
    namepj = models.CharField(max_length=50)
    listname = models.CharField(max_length = 50)
    professor = models.CharField(max_length=50)

    def __str__(self):
        return self.namepj