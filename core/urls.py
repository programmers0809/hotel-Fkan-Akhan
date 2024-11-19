from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns  # i18n_patterns ni import qilish

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Tilni qo'llab-quvvatlaydigan URL-larni qo'shish
urlpatterns += i18n_patterns(
    path('', include('hotel.urls')),  # Bu yerda tilga mos ravishda URL-larni qo'shish
)
