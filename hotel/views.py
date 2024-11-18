from django.shortcuts import render

from django.views import View

from .models import ExploreItem ,Testimonial 

class HomeView(View):
    def get(self, request):
        explore_items = ExploreItem.objects.all()
        testimonials = Testimonial.objects.all()
        
        
        context = {
            'explore_items': explore_items,
            'testimonials': testimonials,
       
        }
        return render(request, 'home.html', context=context)