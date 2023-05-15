from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    ListView,FormView,DetailView,CreateView,UpdateView,DeleteView)
from django.views.generic.base import TemplateView,RedirectView
from django.shortcuts import redirect,get_object_or_404
from .models import Post
#mixin
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin


def index(request):
    name='bahman'
    context={"name":name}
    return render(request,'index.html',context)

###TemplateView

class IndexView(LoginRequiredMixin,TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] ='bahman' 
        return context
    

###RedirectView
def github_redirect(request):
    return redirect('https://github.com')

class RedirectToMaktabkhoone(LoginRequiredMixin,RedirectView):
    url='https://maktabkhooneh.org'
    # permanent=False
    # query_string=False
    # pattern_name=''

    
class RedirectToMaktabkhooneTwo(LoginRequiredMixin,RedirectView):
    url='https://maktabkhooneh.org'
    # permanent=False
    # query_string=False
    # pattern_name=''

    def get_redirect_url(self, *args: Any, **kwargs: Any):
        post=get_object_or_404(Post,pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)

####ListView
class PostListView(LoginRequiredMixin,ListView):
    # model=Post
    queryset=Post.objects.all()
    context_object_name='posts'
    ordering='-id'
    paginate_by=4
    
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


class PostDetailView(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    permission_required='blog.view_post'
    model=Post
    context_object_name='post'


#formview
from .forms import ContactForm,ContactUsForm


class PostFormView(LoginRequiredMixin,FormView):
    template_name='blog/contact.html'
    form_class=ContactForm
    success_url='/blog/posts/'


class PostCreateFormView(LoginRequiredMixin,FormView):
    template_name='blog/contact.html'
    form_class=ContactUsForm
    success_url='/blog/posts/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

#createview

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content','status','category','published_date']
    success_url='/blog/posts/'

    def form_valid(self, form):
        form.instance.auhtor = self.request.user
        return super().form_valid(form)

class PostCreateViewForm(LoginRequiredMixin,CreateView):
    model=Post
    form_class=ContactUsForm
    success_url='/blog/posts/'

    # def form_valid(self, form):
    #     form.instance.auhtor = self.request.user
    #     return super().form_valid(form)


#updateview(edit)

class PostEditView(LoginRequiredMixin,UpdateView):
    model=Post
    form_class=ContactUsForm
    success_url='/blog/posts/'
    
    # fields=['',]
    # template_name=''


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url='/blog/posts/'



