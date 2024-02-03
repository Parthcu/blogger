from django.shortcuts import render
from rest_framework import generics
from .models import ProfilePic, BlogPost, TextPost,ResearchPost
from .serializers import ProfilePicSerializer, BlogPostModelSerializer, TextPostSerializer, ResearchPostModelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

class ProfilePicListCreate(generics.ListCreateAPIView):
    queryset = ProfilePic.objects.all()
    serializer_class = ProfilePicSerializer
    authentication_classes = [BasicAuthentication]  # Use Basic Authentication
    permission_classes = [IsAuthenticated]  # Use TokenAuthentication
    

class BlogPostModelListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostModelSerializer
    authentication_classes = [BasicAuthentication]  # Use Basic Authentication
    permission_classes = [IsAuthenticated]  # Use TokenAuthentication
    
class ResearchPostModelListCreate(generics.ListCreateAPIView):
    queryset = ResearchPost.objects.all()
    serializer_class = ResearchPostModelSerializer
    authentication_classes = [BasicAuthentication]  # Use Basic Authentication
    permission_classes = [IsAuthenticated]  # Use TokenAuthentication
    

class TextPostListCreate(generics.ListCreateAPIView):
    queryset = TextPost.objects.all()
    serializer_class = TextPostSerializer
    authentication_classes = [BasicAuthentication]  # Use Basic Authentication
    permission_classes = [IsAuthenticated]  # Use TokenAuthentication
    

class SuperuserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    