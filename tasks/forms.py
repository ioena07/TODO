from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["title", "link", "duration"]


class CategoriesForm (forms.ModelForm):
    class Meta:
        model = Category_type
        fields = "__all__"


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["title", "link", "duration", "complete"]
