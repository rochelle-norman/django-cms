from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "url")

# Register your models here.
admin.site.register(Project, ProjectAdmin)