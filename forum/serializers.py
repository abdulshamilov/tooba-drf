from rest_framework import serializers
from .models import Thread, Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author_name', 'content', 'likes', 'dislikes', 'created_at']

class ThreadSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Thread
        fields = ['id', 'title', 'description', 'created_at', 'posts']
