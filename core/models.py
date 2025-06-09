from django.db import models
from django.core.exceptions import ValidationError
import os
# Create your models here.

class AbstractModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

def validate_file_size(value):
    max_size = 5 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError('File is too large, size should be under 5 MB')
    
def validate_file_type(value):
    typefile = os.path.splitext(value.name)[1].lower()
    print(typefile)
    allowed_extensions = ['.pdf', '.docx', '.txt', '.png', '.jpg', '.jpeg']
    if typefile not in allowed_extensions:
        raise ValidationError('Wrong file type! Allowed file types are: PDF, DOCX, TXT, PNG, JPG')

class Check_up(AbstractModel):
    file = models.FileField(upload_to='uploads/', validators=[validate_file_size, validate_file_type])
    comment = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=13)
    accept_policy = models.BooleanField(default=False)

    def __str__(self):
        return self.comment 
    