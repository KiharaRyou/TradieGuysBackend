from django.urls import path
from orders import views

urlpatterns = [
    path('', views.ListCreateOrder.as_view()),
    path('<int:pk>/', views.OrderDetail.as_view()),
    ]