from datetime import datetime
from django.test import SimpleTestCase,TestCase
from ..models import Post,Category
from django.contrib.auth import get_user_model
from accounts.models import Profile,User



"""
# User2=get_user_model()

data has error + no author id + profile
class TestPostModel(TestCase):
    def test_create_post_with_valid_data(self):
        category_obj=Category.objects.create(name='cat_one')

        post=Post.objects.create(data={
            "title":"test title",
            "content":"content",
            "status":True,
            "published_date":datetime.now(),
            "category":category_obj, 
        }
        )
        self.assertEquals(post.title,'test title')

class TestPostModel(TestCase):
    def test_create_post_with_valid_data(self):
        category_obj=Category.objects.create(name='cat_one')
        user=User.objects.create_user(email="bahmanpn@gmail.com",password='Zx!@1234')

        # user=User.objects.create(email="bahmanpn@gmail.com",password='Zx!@1234')
        # user=User2.objects.create(email="bahmanpn@gmail.com",password='Zx!@1234')
        # user=User2.objects.create_user(email="bahmanpn@gmail.com",password='Zx!@1234')

        profile=Profile.objects.create(
            user=user,
            first_name='test_first_name',
            last_name='test_last_name',
            description='test desc'
        )

        post=Post.objects.create(
            auhtor=profile,
            # auhtor = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)==>author=profile
    
            title="test title",
            content="content",
            status=True,
            published_date=datetime.now(),
            category=category_obj
        )
        self.assertEquals(post.title,'test title')
"""

class TestPostModel(TestCase):

    def setUp(self):
        self.user=User.objects.create_user(email="bahmanpn@gmail.com",password='Zx!@1234')

        # user=User.objects.create(email="bahmanpn@gmail.com",password='Zx!@1234')
        # user=User2.objects.create(email="bahmanpn@gmail.com",password='Zx!@1234')
        # user=User2.objects.create_user(email="bahmanpn@gmail.com",password='Zx!@1234')

        self.profile=Profile.objects.create(
            user=self.user,
            first_name='test_first_name',
            last_name='test_last_name',
            description='test desc'
        )

    def test_create_post_with_valid_data(self):
        category_obj=Category.objects.create(name='cat_one')

        post=Post.objects.create(
            auhtor=self.profile,
            # auhtor = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)==>author=profile
    
            title="test title",
            content="content",
            status=True,
            published_date=datetime.now(),
            category=category_obj
        )
        self.assertEquals(post.title,'test title')
        self.assertTrue(Post.objects.filter(pk=post.id).exists())