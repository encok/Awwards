from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class project(models.Model):
    project_name = models.CharField(max_length=120)
    # ingredient = models.CharField(max_length=600)
    category = models.CharField(max_length=120)
    project_pic = models.ImageField(upload_to="images")
    description = models.CharField(max_length=600)
    created_by = models.ForeignKey(to=User,on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name


