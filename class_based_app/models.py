from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Diary(models.Model):
    title = models.CharField(max_length=200, unique=True)
    date_time = models.DateTimeField(auto_now=True)
    content = models.TextField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.date_time} {self.content} {self.user}"
    
    class Meta:
        verbose_name = "Diary"