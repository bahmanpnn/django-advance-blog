from rest_framework import serializers
from ...models import Post

# class PostSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=255)
#     id=serializers.IntegerField()


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        # fields='__all__'
        fields=['id','auhtor','category','status','title','content','created_date','published_date']