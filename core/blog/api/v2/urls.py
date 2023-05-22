from django.urls import path
from .views import *

# app_name='api-v1'

urlpatterns = [
    path('posts/',PostList.as_view(),name='postlist-apiview'),
    path('posts/<int:pk>/',PostDetail.as_view(),name='post-detail-apiview'),

    #viewset
    path('posts/viewset/',PostViewSet.as_view({'get':'list','post':'create'}),name='posts-viewset-list'),
    path('posts/viewset/<int:pk>/',PostViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='posts-viewset-retrieve'),
]

'''

def hello()
    pass
    
get=hello==> 'get':'list','post':'create'

'''