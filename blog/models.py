from django.db import models

# Create your models here.


class blog(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
