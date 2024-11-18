from django.db import models


from django.db import models

class ExploreItem(models.Model):
    CATEGORY_CHOICES = [
        ('restaurant', 'Restaurant'),
        ('hotel', 'Hotel'),
        ('destination', 'Destination'),
        ('real_estate', 'Real Estate'),
        ('automotion', 'Automotion'),
    ]
    

    
    title = models.CharField(max_length=255, verbose_name = 'Nomi')
    description = models.TextField(verbose_name = 'Haqida')
    rating = models.FloatField(verbose_name = 'Reyting')
    ratings_count = models.PositiveIntegerField()
    price_from = models.CharField(max_length=50, verbose_name = 'Narxi')
    price_to = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='', verbose_name='Mehmonxona rasmi')
    person_image = models.ImageField(upload_to='hotel/people/', verbose_name='Odam rasmi')
    person_name = models.CharField(max_length=255)
    is_open = models.BooleanField(default=False, verbose_name='Ochiq yoki yopiq')
    button_label = models.CharField(max_length=50, default="best rated")
    map_link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Mehmonxona'
        verbose_name_plural = 'Mehmonxonalar'
   


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clients/', blank=True, null=True)  # Bu maydon rasmi yuklash imkoniyatini beradi
    rating = models.IntegerField(default=5)  # 1 dan 5 gacha yulduzlar sonini belgilash
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.location}"
    
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'comment'
        verbose_name_plural = 'coomentt'
# from django.db import models

# class Topic(models.Model):
#     name = models.CharField(max_length=100)  # Topic nomi
#     icon = models.ImageField(upload_to='icons/')  # Ikonka (rasm saqlanadigan joy)
#     additional_icon = models.ImageField(upload_to='additional_icons/', null=True, blank=True)  # Yana bir ikonka (yoki qo'shimcha rasm)
#     listings = models.PositiveIntegerField()  # Listings soni

#     def __str__(self):
#         return self.name


