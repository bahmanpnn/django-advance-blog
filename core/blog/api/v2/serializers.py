from rest_framework import serializers
from ...models import Post,Category
from accounts.models import Profile

class PostSerializer(serializers.ModelSerializer):
        #extra fields that do not have connections with request and can handle simply
    created_date=serializers.CharField(read_only=True)
    published_date=serializers.ReadOnlyField()

    snippet=serializers.ReadOnlyField(source='content_snippet')
    relative_url=serializers.URLField(source='get_absolute_api_url',read_only=True)
    auhtor=serializers.ReadOnlyField(source='get_post_author')
    
        #extra field that have connection with request and its better to all of proccessing of these objects be in serializer to handle better
    # category=serializers.SlugRelatedField(many=False,slug_field='name',read_only=True)
    # category=serializers.SlugRelatedField(many=False,slug_field='name',queryset=Category.objects.all())

    abs_url=serializers.SerializerMethodField(method_name='get_abs_url')

    class Meta:
        model=Post
        # fields='__all__'
        fields=['id','auhtor','category','image','status','title','content','created_date','published_date','snippet','relative_url','abs_url']
        read_only_fields=['status']


    def get_abs_url(self,obj):
        '''
        this method get request dictionary and add object.pk after request url==>/blog/api/v2/modelviewset/obj.pk
        '''
        req=self.context.get('request')
        return req.build_absolute_uri(obj.pk)
    
    def to_representation(self, instance):
        rep=super().to_representation(instance)
        req=self.context.get('request')

        if req.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet')
            rep.pop('abs_url')
            rep.pop('relative_url')
        else:
            rep.pop('content')

        rep['category']=CategorySerializer(instance.category,context={'request':req}).data
        return rep

    
    def create(self, validated_data):
        # validated_data['auhtor']=self.context.get('request').user.id ==>it does not work because we set the profile for author of post
        
        # user=User.objects.get(self.context.get('request').user.id)==>it works but it is bad to query twice to database!first for checking user.id and second to checking profile with user!
        # user=self.context.get('request').user.id ==>it works but it seems to again query twice to database!first for checking user.id and second to checking profile with user!
        # validated_data['auhtor']=Profile.objects.get(user=user)

        #best way
        # post->author->profile->user-->id--> post_auhtor__profile_user__id
        validated_data['auhtor']=Profile.objects.get(user__id=self.context.get('request').user.id)

        return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        # fields='__all__'
        fields=['id','name']

    # def to_representation(self, instance):
    #     rep=super().to_representation(instance)
    #     try:
    #         req=self.context.get('request')
    #         rep['req']=req
    #         return rep
    #     except:
    #         rep['error']='request did not get!'
    #         return rep
