from django.shortcuts import render
from django.views import generic

from api.blog.forms import NewArticleForm

class ProfileView(generic.TemplateView):

    template_name = 'profile.html'

    def create_article_form(self):
        return NewArticleForm()
