from django.db import models

# Create your models here.

class ClassProject(models.Model):
    nameproject = models.CharField(max_length=50)
    listname = models.CharField(max_length = 50)
    professorname = models.CharField(max_length=50)
    detailproject = models.TextField(default = "Input Detail Project")

    def __str__(self):
        return self.nameproject

class Project(models.Model):
    name_project = models.CharField(db_column='name_project',max_length=50)
    list_name = models.CharField(db_column='list_name',max_length = 50)
    professor_name = models.CharField(db_column='professor_name',max_length=50)
    detail_project = models.TextField(db_column='detail_project',max_length=3000)

    def __str__(self):
        return self.name_project