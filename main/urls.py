from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name = 'about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
    path("api-auth/", include("rest_framework.urls")),
]
