from django.db import models
from django.conf import settings
from datetime import timedelta

# Create your models here.
#https://stackoverflow.com/questions/50599932/foreignkey-missing-required-positional-argument-on-delete-when-trying-to-create
#  """One more recommendation: it's a best practice to name your model in singular. Django will automatically "pluralize" them.
#  If Django fails to pluralize the class name properly, you can specify your own plural by adding the following to the models Meta:
# class Meta:
#     verbose_name_plural = "salaries""""
#https://stackoverflow.com/questions/15696348/django-custom-command-complains-assertionerror-foreignkeynone-is-invalid-why

#forms.ModelChoiceField(queryset=School.objects.all(), initial=0)


class Category_type (models.Model):
    Category = models.CharField(max_length = 255, default = "")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.Category

#sau "on_delete = models.PROTECT"


class Tasks (models.Model):
    category = models.ForeignKey(Category_type, default = 2, on_delete = models.SET_DEFAULT)
    title = models.CharField (max_length = 255)
    complete = models.BooleanField (default = False)
    duration = models.DurationField(default = timedelta(minutes = 30))
    link = models.URLField (max_length = 2083, blank = True)
    created = models.DateTimeField (auto_now_add = True)
    completed = models.DateTimeField (auto_now_add = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete = models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title

