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



from .models import ContactInfo

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'facebook_url', 'twitter_url', 'linkedin_url', 'google_plus_url')
    search_fields = ('phone_number',)


from .models import Topic

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'listings_count', 'image')
    search_fields = ('name',)