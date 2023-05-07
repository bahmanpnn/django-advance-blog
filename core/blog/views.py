from typing import Any, Optional
from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from django.shortcuts import redirect,get_object_or_404
from .models import Post

def index(request):
    name='bahman'
    context={"name":name}
    return render(request,'index.html',context)



class IndexView(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] ='bahman' 
        return context
    

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