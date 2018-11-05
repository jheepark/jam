from django import forms
from api.blog.models import Article


class NewArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
