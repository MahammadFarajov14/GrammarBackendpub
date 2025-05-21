from django.db import models
from core.models import AbstractModel
# Create your models here.

class RuleCategory(AbstractModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Rule(AbstractModel):
    category = models.ForeignKey(RuleCategory, related_name='rule', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        if self.category:
            return f'{self.category} - {self.title}'
        return self.title