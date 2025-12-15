from django.contrib import admin
from .models import Experience, Education, Professionalskill, language


@admin.register(Experience)
# this class that lets you customize the admin interface for the Experience model
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'office_name', 'from_date', 'to_date')
    search_fields = ('position', 'office_name', 'company_address')
    list_filter = ('from_date', 'to_date')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution_name', 'from_date', 'to_date')
    search_fields = ('degree', 'institution_name', 'address')
    list_filter = ('from_date', 'to_date')


@admin.register(Professionalskill)
class ProfessionalskillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(language)
class languageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
# Register your models here.
