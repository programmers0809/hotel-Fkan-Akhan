from django import forms
from .models import Testimonial


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search')  # Matn bo'yicha qidiruv
    category = forms.ChoiceField(choices=[('', 'All Categories'), ('restaurant', 'Restaurant'), ('hotel', 'Hotel'), ('destination', 'Destination'), ('real_estate', 'Real Estate'), ('automotion', 'Automotion')], required=False, label='Category')
    price_from = forms.CharField(max_length=50, required=False, label='Price From')  # Narx diapazoni
    price_to = forms.CharField(max_length=50, required=False, label='Price To')  # Narx diapazoni


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['client_name', 'location', 'image', 'rating', 'comment']  # Ko'rsatilgan maydonlarni o'z ichiga oladi
    
    # Qo'shimcha tarzda, rating maydoniga ba'zi cheklovlar qo'yishingiz mumkin
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating 1 dan 5 gacha bo'lishi kerak.")
        return rating