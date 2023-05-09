
from django.urls import path
from .views import *
from django.views.generic import TemplateView,RedirectView


app_name='blog'

urlpatterns = [
    path('fbv_index',index,name='fbv-index'),
    path('cbv_index',TemplateView.as_view(template_name="index.html",extra_context={"name":'hamid'}),name='cbv-index'),
    path('my_cbv_index',IndexView.as_view(),name='my-cbv-index'),
    path('go-to-github',RedirectView.as_view(url='https://github.com'),name='go-to-github'),
    path('go-to-cbv-index',RedirectView.as_view(pattern_name="blog:cbv-index"),name='go-to-cbv-index'),
    path('fbv-go-to-github',github_redirect,name='fbv-index'),
    path('cbv-go-to-maktabkhoone',RedirectToMaktabkhoone.as_view(),name='redirect-to-maktabkhoone-cbv'),
    path('cbv-go-to-maktabkhoone-two/<int:pk>',RedirectToMaktabkhooneTwo.as_view(),name='redirect-to-maktabkhoone-cbv-two'),
    path('posts/',PostListView.as_view(),name='posts-list'),
    path('posts/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    
]
