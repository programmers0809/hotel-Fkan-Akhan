from django.contrib import admin
from .models import ExploreItem, Testimonial

@admin.register(ExploreItem)
class ExploreItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'rating', 'is_open')
    list_filter = ('category', 'is_open')
    search_fields = ('title', 'category')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'location', 'rating')  # Mos ravishda o'z maydonlaringizni tanlang
    list_filter = ('location', 'rating')  # Agar kerak bo'lsa, filterlar
    search_fields = ('client_name', 'location')  # Qidiruv maydonlari



