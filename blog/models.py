from django.db import models
from core.models import AbstractModel
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Blog(AbstractModel):
    user = models.ForeignKey(User, related_name='blog', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    description = models.TextField()

    def len(self):
        return len(self.objects.all())

    def __str__(self):
        return self.title
    
class Comment(AbstractModel):
    blog = models.ForeignKey(Blog, related_name='blog_comment', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    description = models.TextField()

    def len(self):
        return len(self.objects.all())

    def __str__(self):
        return self.title