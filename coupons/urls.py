from django.urls import path
from coupons import views

urlpatterns = [
    path('', views.CouponList.as_view()),
    path('<int:pk>/', views.CouponDetail.as_view()),
    path('active/', views.get_active_coupons),
    path('similar/', views.get_similar_coupons)
    ]