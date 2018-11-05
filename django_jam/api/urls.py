
from django.contrib import admin
from django.urls import path, include
from api.blog import views
from rest_framework import routers
from api.blog import views as blog_views
from rest_framework.documentation import include_docs_urls


app_name = 'api'

router = routers.DefaultRouter()
router.register('blog/articles', blog_views.ArticleView),
router.register('blog/tags', blog_views.TagView),

urlpatterns = [

    path('', include(router.urls)),

]
