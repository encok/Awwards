from django.db import models
from django.views.generic import TemplateView

# Create your models here.
@classmethod
def search_by_projects(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        print(projects)
        return projects 