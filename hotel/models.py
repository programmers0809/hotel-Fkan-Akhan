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
