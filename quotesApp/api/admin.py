from django.contrib import admin
from .models import QuotesModel

@admin.register(QuotesModel)
class QuotesModelAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'topic')