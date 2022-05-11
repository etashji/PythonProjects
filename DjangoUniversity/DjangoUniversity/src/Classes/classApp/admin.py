from django.contrib import admin
#This imports the model
from .models import djangoClasses
#This imports the djangoClasses model.
admin.site.register(djangoClasses)
