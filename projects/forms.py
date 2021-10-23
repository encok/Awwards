from django.forms import ModelForm
from .models import project
from django import forms

class CreateRecipeForm(ModelForm):
    class Meta:
        model = project
        fields = "__all__"
        widgets = {'description':forms.Textarea(),
                   'created_by':forms.HiddenInput()}