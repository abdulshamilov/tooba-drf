from django.db import models

class Thread(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="Без описания")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(Thread, related_name="posts", on_delete=models.CASCADE)
    author_name = models.CharField(max_length=50, default="Аноним")
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
