from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Diary(models.Model):
    title = models.CharField(max_length=200, unique=True)
    date_time = models.DateTimeField(auto_now=True)
    content = RichTextField(blank=True, null=True)
    image_url = models.CharField(max_length=500, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.date_time} {self.content} {self.image_url} {self.user}"
    
    class Meta:
        verbose_name = "Diary"


class Image(models.Model):
    image = models.ImageField(upload_to="images")
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name="images")

    def __str__(self):
        return f"{self.image} {self.user}"


class Background(models.Model):
    image = models.ImageField(upload_to="images")
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name="background")

    def __str__(self):
        return f"{self.image} {self.user}"
    