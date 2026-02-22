from django.contrib import admin
from . import models


admin.site.register(models.WebPage)
admin.site.register(models.PageKeyword)
admin.site.register(models.Keyword)
admin.site.register(models.Link)