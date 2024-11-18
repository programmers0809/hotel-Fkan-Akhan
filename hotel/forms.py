from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search')  # Matn bo'yicha qidiruv
    category = forms.ChoiceField(choices=[('', 'All Categories'), ('restaurant', 'Restaurant'), ('hotel', 'Hotel'), ('destination', 'Destination'), ('real_estate', 'Real Estate'), ('automotion', 'Automotion')], required=False, label='Category')
    price_from = forms.CharField(max_length=50, required=False, label='Price From')  # Narx diapazoni
    price_to = forms.CharField(max_length=50, required=False, label='Price To')  # Narx diapazoni
