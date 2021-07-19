from django.urls import path
from articles import views

urlpatterns = [
    path('', views.ListCreateArticle.as_view()),
    path('<int:pk>/', views.ArticleDetail.as_view()),
    path('get/', views.get_articles),
    ]