from django.contrib import admin

from .models import ExploreItem

@admin.register(ExploreItem)

class ExploreItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'rating', 'is_open')
    list_filter = ('category', 'is_open')
    search_fields = ('title', 'category')
