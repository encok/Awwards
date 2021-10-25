from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class project(models.Model):
    project_name = models.CharField(max_length=120)
    # ingredient = models.CharField(max_length=600)
    project_link = models.CharField(max_length=120)
    project_pic = CloudinaryField('image')
    description = models.CharField(max_length=600)
    created_by = models.ForeignKey(to=User,on_delete=models.CASCADE)


    def __str__(self):
        return self.project_name

    # @classmethod
    # def search_by_title(cls,search_term):
    #     projects = cls.objects.filter(title__icontains=search_term)
    #     return projects
class Rating(models.Model):
    image = models.ImageField(upload_to='images/')
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return str(self.pk)

