from rest_framework import serializers
from ...models import Post,Category


class PostSerializer(serializers.ModelSerializer):
        #extra fields that do not have connections with request and can handle simply
    created_date=serializers.CharField(read_only=True)
    published_date=serializers.ReadOnlyField()

    snippet=serializers.ReadOnlyField(source='content_snippet')
    relative_url=serializers.URLField(source='get_absolute_api_url',read_only=True)
    
        #extra field that have connection with request and its better to all of proccessing of these objects be in serializer to handle better
    # category=serializers.SlugRelatedField(many=False,slug_field='name',read_only=True)
    category=serializers.SlugRelatedField(many=False,slug_field='name',queryset=Category.objects.all())

    abs_url=serializers.SerializerMethodField(method_name='get_abs_url')

    class Meta:
        model=Post
        # fields='__all__'
        fields=['id','auhtor','category','status','title','content','created_date','published_date','snippet','realtive_url','abs_url']
        read_only_fields=['status']


    def get_abs_url(self,obj):
        '''
        this method get request dictionary and add object.pk after request url==>/blog/api/v2/modelviewset/obj.pk
        '''
        req=self.context.get('request')
        return req.build_absolute_uri(obj.pk)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        # fields='__all__'
        fields=['id','name']
