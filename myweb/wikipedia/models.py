from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()
    author = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('author',)

    def __str__(self):
        return self.title
    objects = models.Manager()


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Komentarz {} dodany {}' .format(self.name, self.created)
    objects = models.Manager()
