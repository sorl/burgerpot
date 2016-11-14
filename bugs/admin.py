from django.contrib import admin
from .models import Bug


@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    pass
