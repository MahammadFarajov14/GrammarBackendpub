from rest_framework import serializers
from blog.models import Comment, Blog

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = (
            'id',
            'blog',
            'title',
            'description',
        )

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = (
            'id',
            'user',
            'title',
            'description',
        )