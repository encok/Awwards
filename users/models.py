from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.


class Profile(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     profile_pic = CloudinaryField('image')
     bio = models.CharField(max_length=120)
     birth_date = models.DateField(null=True)

     def __str__(self):
         return str(self.user)