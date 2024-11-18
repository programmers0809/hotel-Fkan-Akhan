from django.urls import path

from .views import HomeView, search_view

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),  
    path('search/', search_view, name='search'),
]
