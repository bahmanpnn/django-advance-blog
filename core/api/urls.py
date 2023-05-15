from django.urls import path
from .views import *

urlpatterns = [
    path('posts/' ,api_post_list_view ,name='postslist-api'),
]