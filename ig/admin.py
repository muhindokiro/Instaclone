from django.contrib import admin
from .models import Pic

class PicAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
    
admin.site.register(Pic)

# Register your models here.
