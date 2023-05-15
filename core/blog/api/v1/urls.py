
from django.urls import path,include
from .views import *

# app_name='api-v1'

urlpatterns = [

    path('posts/' ,post_list ,name='post_list_api'),

]