from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.posts , name='posts'),
    path('posts/<str:pk>/', views.post_view, name='post-view'),
    path('create-post/', views.create_post, name='create-post'),
    path('update-post/<str:pk>/', views.update_post, name='update-post'),
    path('delete-post/<str:pk>/', views.delete_post, name='delete-post')
]