from django.contrib import admin

#from models import Painter
from models import Painting
#from models import Painting_Image

#admin.site.register(Painter)

class PaintingAdmin(admin.ModelAdmin):
    list_display = ('id','title','painter','price_original_currency','currency','year','sale_date','height','width')

admin.site.register(Painting,PaintingAdmin)

#admin.site.register(Painting_Image)

# class Painting_Image(admin.ModelAdmin):
#     readonly_fields = ('image_tag',)

#admin.site.register(Painting,PaintingAdmin)