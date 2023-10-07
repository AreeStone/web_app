from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from .serializers import NewsSerializer
from news.models import Articles
from .permissions import IsAuthorOrReadOnly  # new

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class NewsList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Articles.published.all()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author']
    search_fields = ['full_text']
    ordering_fields = ['author_id', 'anons', 'date', 'updated']
    ordering = ['full_text']
    pagination_class = StandardResultsSetPagination


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Articles.published.all()
    serializer_class = NewsSerializer


class UserNewsList(generics.ListAPIView):
    queryset = Articles.published.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        user = self.kwargs['username']
        return Articles.published.filter(author=user)

