from blog.api.views import CommentCreateAPIView, BlogCreateAPIView
from django.urls import path

urlpatterns = [
    path('comments/', CommentCreateAPIView.as_view(), name='comments'),
    path('blogs/', BlogCreateAPIView.as_view(), name='blogs'),

]