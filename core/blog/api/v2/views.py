from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework import status
from ...models import Post
# from blog.models import Post
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListAPIView,ListCreateAPIView
from rest_framework import mixins

"""
class PostList(APIView):
    permission_classes=(IsAuthenticatedOrReadOnly,)
    serializer_class=PostSerializer
    def get(self,request):
        posts=Post.objects.filter(status=True)
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data,status=200)
    
    def post(self,request):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=201)


class PostList(GenericAPIView):
    permission_classes=(IsAuthenticatedOrReadOnly,)
    serializer_class=PostSerializer
    queryset=Post.objects.filter(status=True)
    
    def get(self,request):
        # my_query=self.queryset
        my_query=self.get_queryset()
        serializer=self.serializer_class(my_query,many=True)
        
        return Response(serializer.data,status=200)
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=201)



class PostList(GenericAPIView,mixins.ListModelMixin):
    permission_classes=(IsAuthenticatedOrReadOnly,)
    serializer_class=PostSerializer
    queryset=Post.objects.filter(status=True)
    
    def get(self,request,*args,**kwargs):
        '''
        this method is for listing of query and posts to return data with json format
        '''

        return self.list(request,*args,**kwargs)
    

class PostList(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    '''
    this is a ListCreateGenericAPIView that we made with 2 mixins.
    but there is new way to create postlist class that i created after this class
    '''
    permission_classes=(IsAuthenticatedOrReadOnly,)
    serializer_class=PostSerializer
    queryset=Post.objects.filter(status=True)
    
    def get(self,request,*args,**kwargs):
        '''
        this method is for listing of query and posts to return data with json format
        self.list method is from ListModelMixin and its methods that we use it
        '''

        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        '''
        this method is for creating new post with post method(but i think there is create method in mixins too!)
        self.create method is from CreateModelMixin and its methods that we use it
        '''
        return self.create(request,*args,**kwargs)

        
class PostList(ListAPIView):

    permission_classes=(IsAuthenticatedOrReadOnly,)
    serializer_class=PostSerializer
    queryset=Post.objects.filter(status=True)


"""
    
    
class PostList(ListCreateAPIView):

    permission_classes=(IsAuthenticatedOrReadOnly,)
    serializer_class=PostSerializer
    queryset=Post.objects.filter(status=True)
    


class PostDetail(APIView):
    permission_classes=(IsAuthenticatedOrReadOnly,)
    serializer_class=PostSerializer

    def get(self,request,pk):
        obj=get_object_or_404(Post,pk=pk,status=True)
        # serializer=PostSerializer(obj)
        serializer=self.serializer_class(obj)
        return Response(serializer.data,status=200)
    
    def put(self,request,pk):
        obj=get_object_or_404(Post,pk=pk,status=True)
        serializer=self.serializer_class(obj,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,pk):
        obj=get_object_or_404(Post,pk=pk,status=True)
        obj.delete()
        return Response({'detail':'item deleted successfully'},status=204)
    

