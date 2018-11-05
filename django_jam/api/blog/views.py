from api.blog.models import Article, Tag
from api.blog.serializers import ArticleSerializer, TagSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
# /api/blog/articles
class ArticleView(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# /api/blog/tags
class TagView(viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
