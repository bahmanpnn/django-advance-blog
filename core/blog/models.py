from django.db import models
from datetime import datetime
from django.urls import reverse
# from django.contrib.auth import get_user_model
# from accounts.models import User
# from django.conf import settings
# from accounts.models import Profile

#getting user model object

# User=get_user_model()

class Post(models.Model):
    '''
    this is a class to define posts for blog app
    '''

    # auhtor=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # auhtor=models.ForeignKey("User", on_delete=models.CASCADE)
    # auhtor=models.ForeignKey(User, on_delete=models.CASCADE)

    # auhtor=models.ForeignKey(Profile, on_delete=models.CASCADE)
    auhtor=models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True)
    title=models.CharField(max_length=250)
    content=models.TextField()
    status=models.BooleanField(default=True)
    category=models.ForeignKey("Category", on_delete=models.SET_NULL,null=True)

    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.title
    
    def content_snippet(self):
        """
        this method is return snippet of content and use in serializer to use in postlist serializer
        to user see complete content in post detail page
        """
        
        return self.content[0:3]
    
    def get_absolute_url(self):
        return reverse("blog:api-v2:router-post-viewset-detail", kwargs={"pk": self.pk})
    
    
    
class Category(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name
    

