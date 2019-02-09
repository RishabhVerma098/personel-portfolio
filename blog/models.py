from django.db import models

# Create your models here.
# for strftime google it , find python doc


class blog(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):  # for django admin customizations
        return self.title

    def summary(self):
        return self.body[:50]

    def pub_date(self):
        return self.date.strftime('%b %e %Y')
