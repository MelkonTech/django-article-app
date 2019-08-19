from articles.models import Article
from .serializers import ArticleSerializers
from rest_framework import viewsets


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()