from django.contrib import admin

# Register your models here.
from .models import ProgramLanguage

# admin.site.register(ProgramLanguage)

@admin.register(ProgramLanguage)
class ProgramLanguageAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)