from django.contrib import admin
from nsapp import models
# Register your models here.

admin.site.register(models.Instructor)
admin.site.register(models.Course)