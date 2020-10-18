from django.contrib import admin
from . import models


admin.site.register(models.StudentData)
admin.site.register(models.Course)