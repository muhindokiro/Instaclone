from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

    def save_editor(self):
        self.save()

    # def delete_editor(self):
    #     self.delete()

    # def display_editor(self):
    #     self.display()

    # def update_editor(self):
    #     self.update()

    

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Post(models.Model):
    username = models.CharField(max_length=60)
    post = models.CharField(max_length=60)
    editor = models.ForeignKey(User,on_delete=models.CASCADE) 
    post_image = models.ImageField(upload_to='images/', blank=True)

    @classmethod
    def todays_ig(cls):
        ig = cls.objects.filter()
        return ig

    @classmethod
    def days_ig(cls,date):
        ig = cls.objects.filter()
        return ig

    @classmethod
    def search_by_username(cls,search_term):
        ig = cls.objects.filter(username__icontains=search_term)
        return ig

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()