from django.urls import path, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .views import NewsList, NewsDetail, UserNewsList

urlpatterns = [
    path("<int:pk>/", NewsDetail.as_view(), name="post_detail"),
    path("", NewsList.as_view(), name="post_list"),
    re_path('^user/(?P<username>.+)/$', UserNewsList.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui")
]