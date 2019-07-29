from django.test import TestCase
from .models import Pic

# Create your tests here.
class PicTestClass(TestCase):

    def setUp(self):

        self.new_pic= Pic(title = 'Test pic',post = 'This is a random test Post')
        self.new_pic.save()

    def tearDown(self):
        Pic.objects.all().delete()
