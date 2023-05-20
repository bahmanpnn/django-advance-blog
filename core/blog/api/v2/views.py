from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework import status
from ...models import Post
# from blog.models import Post
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

class PostList(APIView):
    def get(self,request):
        posts=Post.objects.filter(status=True)
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data,status=200)
    
    def post(self,request):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=201)