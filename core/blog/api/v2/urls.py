from django.urls import path, include
from .views import *
from rest_framework import routers

# app_name='api-v1'


router=routers.DefaultRouter()
router.register('post',PostViewSet,basename='router-post-viewset')

# urlpatterns=router.urls

urlpatterns = [
    #  path('',include(router.urls)),
     path('posts/',PostList.as_view(),name='postlist-apiview'),
     path('posts/<int:pk>/',PostDetail.as_view(),name='post-detail-apiview'),
    #viewset
     path('posts/viewset/',PostViewSet.as_view({'get':'list','post':'create'}),name='posts-viewset-list'),
    path('posts/viewset/<int:pk>/',PostViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='posts-viewset-retrieve'),
 ]

urlpatterns+=router.urls

'''

def hello()
    pass
    
get=hello==> 'get':'list','post':'create'

'''

