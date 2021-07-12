from django.contrib import admin

from phones import models

admin.site.register(
    models.Entry
)
