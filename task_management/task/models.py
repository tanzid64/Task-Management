from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    catagories = models.ManyToManyField(Category)
    assign_date = models.DateField(auto_now_add=True, auto_now= False)

    def __str__(self) -> str:
        return f"{self.title} ({self.assign_date})"