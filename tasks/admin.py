from django.contrib import admin

# Register your models here.

from .models import *  # *means you import all models

admin.site.register(Tasks)
admin.site.register(Category_type)

