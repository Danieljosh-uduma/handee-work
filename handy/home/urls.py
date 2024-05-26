from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.posts , name='posts'),
    path('posts/<str:pk>/', views.post_view, name='post_view')
]