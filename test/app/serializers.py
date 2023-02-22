from rest_framework import serializers
from .models import Post,User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
class APPSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
