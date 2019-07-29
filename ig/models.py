from django.db import models

# Create your models here
class Pic(models.Model): 
    image = models.ImageField(upload_to = 'timeline/')
    caption = models.CharField(max_length =30)