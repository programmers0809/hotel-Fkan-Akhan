from django.shortcuts import render

from django.views import View

from .models import ExploreItem  

class HomeView(View):
    def get(self, request):
        explore_items = ExploreItem.objects.all()
        
        context = {
            'explore_items': explore_items,
        }
        return render(request, 'home.html', context=context)