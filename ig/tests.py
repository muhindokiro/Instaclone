from django.test import TestCase
from .models import Editor,Post,tags
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    # def test_delete_method(self):
    #     self.james.delete_editor()
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors) > 0)

    # def test_update_method(self):
    #     self.james.update_editor()
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors) > 0)

    # def test_display_method(self):
    #     self.james.display_editor()
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Post(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Post.objects.all().delete()

    def test_get_ig_today(self):
        today_ig = Post.todays_ig()
        self.assertTrue(len(today_ig)>0)

    # def test_get_ig_by_date(self):
    #     test_date = '2017-03-17'
    #     date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
    #     ig_by_date = Article.days_ig(date)
    #     self.assertTrue(len(ig_by_date) == 0)
