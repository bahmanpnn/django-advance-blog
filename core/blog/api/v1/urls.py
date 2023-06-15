from django.urls import path, include
from .views import *

# app_name='api-v1'

urlpatterns = [
    path("posts/", post_list, name="post_list_api"),
    path("show_data/", show_data, name="show_data_api"),
    path("posts/<int:id>/", post_detail, name="post_detail_api"),
]
