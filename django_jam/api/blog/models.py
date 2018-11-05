from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):

    name = models.CharField(max_length=32, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Article(models.Model):

    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('date', 'id')
