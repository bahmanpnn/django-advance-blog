from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework import status
from ...models import Post
# from blog.models import Post
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

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
    

