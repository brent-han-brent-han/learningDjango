from django.urls import path

from . import views


urlpatterns = [
    # path('index/', views.index),
    path('', views.index),
    path('index/', views.index),
   path('articles/<int:article_id>/', views.article_page, name='article-detail'),
    path('', views.index),
]