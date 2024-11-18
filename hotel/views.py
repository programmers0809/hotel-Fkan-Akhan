from django.shortcuts import render

from django.views import View

from .models import ExploreItem, Testimonial
from .forms import SearchForm

class HomeView(View):
    def get(self, request):
        explore_items = ExploreItem.objects.all()
        testimonials = Testimonial.objects.all()
        
        
        context = {
            'explore_items': explore_items,
            'testimonials': testimonials,
       
        }
        return render(request, 'home.html', context=context)
    


def search_view(request):
    form = SearchForm(request.GET)
    items = ExploreItem.objects.all()  # Barcha ob'ektlarni olish

    if form.is_valid():
        query = form.cleaned_data.get('query')  # Qidiruv matnini olish
        category = form.cleaned_data.get('category')  # Kategoriyani olish
        price_from = form.cleaned_data.get('price_from')  # Narx diapazonidan boshlash
        price_to = form.cleaned_data.get('price_to')  # Narx diapazonigacha

        # Qidiruv
        if query:
            items = items.filter(title__icontains=query)  # Nomi bo'yicha qidirish
        if category:
            items = items.filter(category=category)  # Kategoriyaga qarab filtrlash
        if price_from:
            items = items.filter(price_from__gte=price_from)  # Narxning minimal qiymati
        if price_to:
            items = items.filter(price_to__lte=price_to)  # Narxning maksimal qiymati

    return render(request, 'search_results.html', {'form': form, 'items': items})