from django.shortcuts import render
from .serializers import PostSerializer
from .models import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView, ListAPIView
# Create your views here.

class Post(ListAPIView):
    queryset = Post.objects.all()
    serializer_class =PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class =PostSerializer
