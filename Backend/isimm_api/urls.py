from django.urls import path
from .views import ArticleListView, ArticleDetailView
app_name='isimm_api'
urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]