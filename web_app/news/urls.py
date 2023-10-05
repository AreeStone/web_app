from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('tag/<slug:tag_slug>/', views.news_home, name='news_list_by_tag'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('<int:pk>/comment/', views.new_comment, name='new_comment'),
]
