from django.contrib import admin
from .models import Project, Technology


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('Project_name', 'description')
    search_fields = ('Project_name',)
    list_filter = ('technologies',)


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology)
