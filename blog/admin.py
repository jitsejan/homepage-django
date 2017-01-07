from django_markdown.admin import MarkdownModelAdmin
from django.contrib import admin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
from . import models

class EntryAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
        )
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}


admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Project)
admin.site.register(models.Website)
admin.site.register(models.Photo)
admin.site.register(models.Photoset)
admin.site.register(models.ImageFile)
