from django.contrib import admin
from .models import History
# Register your models here.

class HistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Article',    {'fields': [
         'article_id', 'article_title', 'article_link']}),
    ]
    list_display = ('article_id', 'article_title', 'article_link')
    list_filter = ['pub_date']


admin.site.register(History, HistoryAdmin)
