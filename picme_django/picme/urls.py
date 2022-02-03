from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>', views.CategoryDetail.as_view(),
         name='category_detail'),
    path('images/', views.ImageList.as_view(), name='image_list'),
    path('images/<int:pk>', views.ImageDetail.as_view(), name='image_detail'),
]
