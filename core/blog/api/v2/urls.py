from django.urls import path
from .views import *

# app_name='api-v1'

urlpatterns = [
    path('posts/',PostList.as_view(),name='postlist-apiview'),
]