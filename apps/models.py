from django.db import models

# Create your models here.

class ProjectTopic(models.Model):
    nameprojectTopic = models.CharField(db_column='nameprojectTopic',max_length=50)
    listproject = models.CharField(db_column='listproject',max_length=50)
    professorname = models.CharField(db_column='professorname',max_length=50)
    year = models.CharField(db_column='year',max_length=50)
    def __str__(self):
        return self.nameprojectTopic
        
class Project(models.Model):
    name_project = models.CharField(db_column='name_project',max_length=50)
    list_name = models.CharField(db_column='list_name',max_length = 50)
    professor_name = models.CharField(db_column='professor_name',max_length=50)
    detail_project = models.TextField(db_column='detail_project',max_length=3000)
    def __str__(self):
        return self.name_project



