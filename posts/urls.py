from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('',post_view,name="posts-list"),
    path('like/',like_post,name="like-post")
]
