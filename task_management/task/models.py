from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateField(auto_now_add=True, auto_now= False)