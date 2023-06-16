from django.test import SimpleTestCase,TestCase
from datetime import datetime
from ..forms import PostForm
from ..models import Category

# class TestPostForm(SimpleTestCase):

#     def test_post_form_with_valid_data(self):
#         test_form=PostForm(data={
#             "title":"test title",
#             "content":"content",
#             "status":True,
#             "published_date":datetime.now(),
#             # "category":"cat1",
#             # "auhtor":"bahmanpn@gmail.com",
#         })
#         self.assertTrue(test_form.is_valid())

class TestPostForm(TestCase):

    def test_post_form_with_valid_data(self):

        category_obj=Category.objects.create(name='hello_cat')

        test_form=PostForm(data={
            "title":"test title",
            "content":"content",
            "status":True,
            "published_date":datetime.now(),
            "category":category_obj,
            # "auhtor":"bahmanpn@gmail.com",
        })
        self.assertTrue(test_form.is_valid())
    
    def test_post_form_with_no_data(self):

        test_form=PostForm(data={})
        self.assertFalse(test_form.is_valid())