from django.contrib import admin
from app15 import models

# Register your models here.
class TopicAdminView(admin.ModelAdmin):
    list_display=('topic_name',)
    search_fields=('topic_name',)

class WebpageAdminView(admin.ModelAdmin):
    list_display=('topic','name','url')
    search_fields=('topic','name')
    list_editable=('name',)
    list_filter=('topic',)

class AccessDetailsAdminView(admin.ModelAdmin):
    list_display=('Webpage','datetime')
    search_fields=('Webpage','datetime')


admin.site.register(models.Topic,TopicAdminView)
admin.site.register(models.Webpage,WebpageAdminView)
admin.site.register(models.AccessDetails,AccessDetailsAdminView)