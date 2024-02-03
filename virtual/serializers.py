from rest_framework import serializers
from .models import ProfilePic, BlogPost, TextPost,ResearchPost

class ProfilePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePic
        fields = ['image']

class BlogPostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title','content','image']

class ResearchPostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchPost
        fields = ['title','content','image']


class TextPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextPost
        fields = ['title', 'email', 'content']
        
        