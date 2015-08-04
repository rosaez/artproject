from django.db import models
from string import join
import os
from PIL import Image as PImage
from artproject.settings import MEDIA_ROOT

#we are gonna have a class with atrtibutes specific to the artist

# class Painter(models.Model):
#     name = models.CharField(max_length=127, null=True, blank=True)
#     nationality = models.CharField(max_length=127, null=True, blank=True)
#     date_of_birth = models.CharField(max_length=127, null=True, blank=True)
#     date_of_death = models.CharField(max_length=127, null=True, blank=True)
#     history = models.TextField()
#     def __unicode__(self):
#         return self.name 

# class Painting_Image(models.Model): # painting images
#     image1 = models.ImageField('img', upload_to= 'paintings/', null=True, blank=True)
#     name = models.CharField(max_length=127, null=True, blank=True)
#     def image_tag(self):
#         return u'<img src="%s" />' % 1 #fill with image url
#     image_tag.short_description = 'Image'
#     image_tag.allow_tags = True 
    
class Painting(models.Model): # individual property characteristics
    
    #image1 = models.ImageField(upload_to = "paintings", null=True, blank=True)
    image1 = models.ImageField('img', upload_to= 'paintings/', null=True, blank=True)
    new_price = models.FloatField(null=True,blank=True)
    price = models.CharField(max_length=127, null=True, blank=True)
    #painter = models.ForeignKey(Painter, null=True)
    painter = models.CharField(max_length=127, null=True, blank=True)
    nationality = models.CharField(max_length=127, null=True, blank=True)
    title = models.CharField(max_length=127, null=True, blank=True)
    markings = models.CharField(max_length=127, null=True, blank=True)
    original_currency = models.CharField(max_length=127, null=True, blank=True)
    price_original_currency = models.IntegerField(null=True, blank=True)
    price_dollars = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=5, null=True, blank=True)
    exhibited = models.TextField(null=True, blank=True)
    edition = models.CharField(max_length=127, null=True, blank=True)
    condition = models.CharField(max_length=127, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    estimate = models.CharField(max_length=127, null=True, blank=True)
    low_estimate = models.IntegerField(null=True, blank=True)
    high_estimate = models.IntegerField(null=True, blank=True)
    measurements = models.CharField(max_length=256, null=True, blank=True)
    url = models.URLField(max_length=511, null=True, blank=True)   
    sizenotes = models.CharField(max_length=127, null=True, blank=True)
    provenance = models.TextField(null=True, blank=True)
    auction_data = models.CharField(max_length=127, null=True, blank=True)
    lot = models.CharField(max_length=127, null=True, blank=True)
    description = models.TextField(null=True, blank=True)      
    literature  = models.TextField(null=True, blank=True)
    materials = models.CharField(max_length=127, null=True, blank=True)
    sale_date = models.CharField(max_length=127, null=True, blank=True) ### fix back to date
    premium_hammer = models.CharField(max_length=127, null=True, blank=True)
    width = models.FloatField(null=True,blank=True)
    height = models.FloatField(null=True,blank=True)
    depth  = models.FloatField(null=True,blank=True)
    nationality = models.CharField(max_length = 127, null=True, blank=True)
    ### aditional cleaning variables ###
    markings_dummy = models.IntegerField(null=True,blank=True)
    provenance_dummy = models.IntegerField(null=True,blank=True)
    auction_house = models.CharField(max_length = 127, null=True,blank=True)
    city_sale = models.CharField(max_length = 127, null=True,blank=True)
    certificate_dummy = models.IntegerField(null=True,blank=True) # not captured in django shell 
    sale_year = models.IntegerField(null=True,blank=True)
    materials_dummy = models.CharField(max_length = 127, null=True,blank=True)
    materials_dummy2 = models.CharField(max_length = 127, null=True,blank=True)
    dead_soon = models.IntegerField(null=True,blank=True)
    quality = models.IntegerField(null=True, blank=True)


    RFC = models.CharField(max_length = 127, null=True, blank=True)
    def __unicode__(self):
        return str(self.id)
