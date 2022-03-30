from django.db import models

# from accounts.models import MyUser
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=255, verbose_name="Post name", help_text="Название поста"
    )
    link = models.URLField(verbose_name="Post link", help_text="Ссылка на пост")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title


class Upvote(models.Model):
    upvoter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_on = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Comment content", help_text="Комментарий")
    created = models.DateTimeField(auto_now_add=True)
