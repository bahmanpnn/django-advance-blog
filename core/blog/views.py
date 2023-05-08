from typing import Any, Optional
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView,RedirectView
from django.shortcuts import redirect,get_object_or_404
from .models import Post

def index(request):
    name='bahman'
    context={"name":name}
    return render(request,'index.html',context)

###TemplateView

class IndexView(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] ='bahman' 
        return context
    

###RedirectView
def github_redirect(request):
    return redirect('https://github.com')

class RedirectToMaktabkhoone(RedirectView):
    url='https://maktabkhooneh.org'
    # permanent=False
    # query_string=False
    # pattern_name=''

    
class RedirectToMaktabkhooneTwo(RedirectView):
    url='https://maktabkhooneh.org'
    # permanent=False
    # query_string=False
    # pattern_name=''

    def get_redirect_url(self, *args: Any, **kwargs: Any):
        post=get_object_or_404(Post,pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)

####ListView
class PostListView(ListView):
    # model=Post
    queryset=Post.objects.all()
    context_object_name='posts'
    ordering='-id'
    paginate_by=1
    
    def get_queryset(self):
        QuerySet=super(PostListView,self).get_queryset()
        QuerySet=QuerySet.filter(status=True)
        return QuerySet
    
    
# class PostListView(ListView):
#     model=Post
#     # queryset=Post.objects.all()
#     context_object_name='posts'
#     # ordering='-id' ==>it does not work because we return objects from this class in get_queryset method not from its parent and super() so ordering and other methods will be have conflicts and problem 
#
#     def get_queryset(self):
#         posts=Post.objects.filter(status=True).order_by('-id')
#         return posts


# class PostListView(ListView):
#     queryset=Post.objects.all()  #i wanted to use queryset(not just model=Post) too and next time i see my codes remember that,
#     #we can use queryset and get_queryset method together in one class!!!
#     # model=Post
#     context_object_name='posts'
    
#     def get_queryset(self):
#         posts=Post.objects.filter(status=True)
#         return posts

# class PostListView(ListView):
#     '''
#     this class is working like next class that commented and used model not queryset!
#     '''
#     queryset=Post.objects.all()
#     context_object_name='posts'


# class PostListView(ListView):
#     model=Post
#     context_object_name='posts'

