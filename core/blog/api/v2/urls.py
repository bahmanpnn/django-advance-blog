#standard libraries

# core django
from django.urls import path, include

# thirdparty packages and apps
from rest_framework import routers

# from app and project
from .views import *



app_name='api-v2'

# router=routers.SimpleRouter()
router=routers.DefaultRouter()

router.register('post',PostViewSet,basename='router-post-viewset')
router.register('post_modelviewset',PostModelViewSet,basename='router-post-model-viewset')
router.register('category',CategoryModelViewSet,basename='router-category-model-viewset')

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

