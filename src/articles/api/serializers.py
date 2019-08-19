from rest_framework import serializers
from articles.models import Article


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title','content')