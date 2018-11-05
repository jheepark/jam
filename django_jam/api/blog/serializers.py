import pickle
from rest_framework import serializers
from api.blog.models import Article, Tag


class ArticleSerializer(serializers.ModelSerializer):

    class TagsField(serializers.CharField):

        def to_representation(self, tags):
            tags = tags.all()
            return "".join([(tag.name + " ") for tag in tags]).rstrip(' ')

    tags = TagsField()

    class Meta:
        model = Article
        fields = '__all__'

    """
        We need to override create() in order to correctly create the related Tags

        TODO: 
    """
    def create(self, validated_data):

        tags = validated_data.pop('tags') # Removes the 'tags' entry from the validated request
        tag_list = []
        for tag in tags.split(' '):
            tag_instance, created = Tag.objects.get_or_create(name=tag)
            tag_list += [tag_instance]

        article = Article.objects.create(**validated_data)
        print(tag_list)
        article.tags.set(tag_list)
        article.save()
        return article


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'
