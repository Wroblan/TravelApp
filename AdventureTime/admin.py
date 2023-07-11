from django.contrib import admin

from AdventureTime import models


admin.site.register(models.Country)
admin.site.register(models.Place)
admin.site.register(models.Capital)
admin.site.register(models.Language)
admin.site.register(models.Currency)
admin.site.register(models.Rating)
admin.site.register(models.Comment)

