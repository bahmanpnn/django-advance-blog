from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework import status
from ...models import Post
# from blog.models import Post
from django.shortcuts import get_object_or_404


data={
    'ttitle':'test',
    'id':1
}

@api_view()
def show_data(request):
    return Response(data)

#compact version

# @api_view(['GET','POST'])
# def post_list(request):
#     if request.method == 'GET':
#         posts=Post.objects.filter(status=True)
#         serializer=PostSerializer(posts,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer=PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


@api_view(['GET','POST'])
def post_list(request):
    if request.method == 'GET':
        posts=Post.objects.filter(status=True)
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

#way 1 is more explainable way that you understand more about codes and use try except but it has more line codes and maybe runtime!
# @api_view()
# def post_detail(request,id):
#     try:
#         obj=Post.objects.get(pk=id)
#         serializer=PostSerializer(obj)

#         # print(obj.__dict__)
#         # print(serializer.__dict__)

#         return Response(serializer.data)
#     except Post.DoesNotExist:
#         return Response('this data does not exists!!',status=404)


#way 2 for make post detailview is this method and few lines coding and handle itself all and it does not need to use try except to handle errors!
@api_view()
def post_detail(request,id):
    obj=get_object_or_404(Post,pk=id,status=True)
    serializer=PostSerializer(obj)
    return Response(serializer.data)