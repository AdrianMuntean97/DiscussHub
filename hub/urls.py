from . import views
from django.urls import path
from .views import DeletePost

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('create_post/', views.CreatePost.as_view(), name='create_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path("delete_post/<slug:slug>/", DeletePost.as_view(), name="delete_post"),
]
