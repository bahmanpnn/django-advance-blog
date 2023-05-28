#standard libraries

# core django libraries
from django.shortcuts import get_object_or_404

# third party packages
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.decorators import action
# from rest_framework.views import APIView
# from rest_framework.generics import GenericAPIView,ListAPIView
# from rest_framework import mixins
# from rest_framework.decorators import permission_classes
# from rest_framework import status

# from app and project
from .serializers import PostSerializer,CategorySerializer
from ...models import Post,Category
from .permissions import *
# from blog.models import Post

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
    


"""
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


class PostDetail(GenericAPIView):
    permission_classes=(IsAuthenticatedOrReadOnly,)
    serializer_class=PostSerializer

    def get(self,request,pk):
        obj=get_object_or_404(Post,pk=pk,status=True)
        # serializer=PostSerializer(obj)
        serializer=self.serializer_class(obj)
        return Response(serializer.data,status=200)


class PostDetail(GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    permission_classes=(IsAuthenticatedOrReadOnly,)
    serializer_class=PostSerializer
    query_set=queryset=Post.objects.filter(status=True)  ==>we can use get_object_model(?) method and override it instead of queryset
    # lookup_field='id'  ==>if you set url with pk it does not need to set this parametr because by default this mixin search pk not id

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
"""

class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticatedOrReadOnly,)
    serializer_class=PostSerializer
    query_set=queryset=Post.objects.filter(status=True)
    # lookup_field='id' 


class PostViewSet(viewsets.ViewSet):
    permission_classes=(IsAuthenticatedOrReadOnly,)
    serializer_class=PostSerializer
    queryset=Post.objects.filter(status=True)

    def list(self,request):
        serializer=self.serializer_class(self.queryset,many=True)
        return Response(serializer.data,status=200)
    
    def retrieve(self,request,pk=None):
        post_obj=get_object_or_404(self.queryset,pk=pk)
        serializer=self.serializer_class(post_obj)
        return Response(serializer.data,status=200)
    
    def create(self,request):
        pass

    def partial_update(self,request):
        pass

    def update(self,request):
        pass

    def destroy(self,request):
        pass
    
class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly)
    serializer_class=PostSerializer
    queryset=Post.objects.filter(status=True)

    @action(methods=['get'],detail=False)
    def send_ok(self,request):
        return Response({'detail':'it is ok! :))'})

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAuthenticatedOrReadOnly,)
    serializer_class=CategorySerializer
    queryset=Category.objects.all()