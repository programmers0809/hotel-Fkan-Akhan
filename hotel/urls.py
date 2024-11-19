from django.urls import path

from .views import HomeView, search_view,comment_view
from django.conf.urls.i18n import set_language

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),  
    path('search/', search_view, name='search'),
    path('comments/', comment_view, name='comment_view'),  # Izohlar ko'rinishi uchun
    path('set_language/', set_language, name='set_language'),

]
