from django.contrib import admin
from .models import Bug, Project
from easy_select2 import select2_modelform


@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = select2_modelform(Project)
