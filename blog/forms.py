from django import forms
from blog.models import Blog, Comment

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = (
            'title',
            'cover_image',
            'description'
        )
        widgets = {
            'title': forms.TextInput(attrs= {
                'placeholder': 'Title *'
            }),
            'description': forms.TextInput(attrs= {
                'placeholder': 'Description *'
            }),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = (
            'title',
            'description',
            'blog'
        )
        widgets = {
            'title': forms.TextInput(attrs= {
                'placeholder': 'Title *'
            }),
            'description': forms.TextInput(attrs= {
                'placeholder': 'Description *'
            }),
            'blog': forms.Select(attrs= {
            }),
        }