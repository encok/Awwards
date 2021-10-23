from django.forms import ModelForm
from .models import project
from django import forms

class CreateRecipeForm(ModelForm):
    class Meta:
        model = project
        fields = "__all__"
        widgets = {'ingredient':forms.Textarea(),'description':forms.Textarea(),
                   'created_by':forms.HiddenInput()}