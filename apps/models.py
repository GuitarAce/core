from django.db import models

# Create your models here.

class ClassProject(models.Model):
    nameproject = models.CharField(max_length=50)
    listname = models.CharField(max_length = 50)
    professorname = models.CharField(max_length=50)
    detailproject = models.TextField(default = "Input Detail Project")

    def __str__(self):
        return self.nameproject