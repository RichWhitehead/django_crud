from django.db import models

# Create your models here.
class Journal(models.Model):
  title = models.CharField(max_length=64)
  author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
  body = models.TextField(default='Enter Descriptions')
  
  def __str__(self):
    return self.title 