from django.contrib import admin
from . import models

admin.site.register(models.Post)
admin.site.register(models.Category1)
admin.site.register(models.Category2)
admin.site.register(models.Settings)
admin.site.register(models.Answer)