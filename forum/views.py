from rest_framework import generics
from .models import Thread, Post
from .serializers import ThreadSerializer, PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Тема: список и создание
class ThreadListCreateView(generics.ListCreateAPIView):
    queryset = Thread.objects.all().order_by("-created_at")
    serializer_class = ThreadSerializer

# Комментарии (обсуждение) и добавление поста
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        thread_id = self.kwargs["thread_id"]
        return Post.objects.filter(thread_id=thread_id).order_by("created_at")

    def perform_create(self, serializer):
        thread_id = self.kwargs["thread_id"]
        author = self.request.data.get("author_name") or "Аноним"
        serializer.save(thread_id=thread_id, author_name=author)

# Лайк/дизлайк
@api_view(['POST'])
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.likes += 1
    post.save()
    return Response({'likes': post.likes})

@api_view(['POST'])
def dislike_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.dislikes += 1
    post.save()
    return Response({'dislikes': post.dislikes})
