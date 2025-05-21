from blog.api.serializers import CommentSerializer, BlogSerializer
from blog.models import Comment, Blog
from rest_framework.generics import ListCreateAPIView

class CommentCreateAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class BlogCreateAPIView(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()