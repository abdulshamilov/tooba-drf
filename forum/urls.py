from django.urls import path
from .views import ThreadListCreateView, PostListCreateView, like_post, dislike_post

urlpatterns = [
    path("threads/", ThreadListCreateView.as_view(), name="thread-list-create"),
    path("threads/<int:thread_id>/posts/", PostListCreateView.as_view(), name="post-list-create"),
    path("posts/<int:post_id>/like/", like_post, name="like-post"),
    path("posts/<int:post_id>/dislike/", dislike_post, name="dislike-post"),
]
