from django.contrib import admin

# Register your models here.
from comparator.scraper.models import Task

admin.site.register(Task)
