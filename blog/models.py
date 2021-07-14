from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=60)
    phone = models.IntegerField(blank=True, null=True, unique=True)
    email = models.EmailField()
    lastIP = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return self.username + "," + self.name

class Blogpage(models.Model):
    title = models.CharField(max_length=12)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.CharField(max_length=100, blank=True, null=True)
    Background = models.CharField(max_length=300)
    isBackgroundHEX = models.BooleanField()

    def __str__(self):
        return self.title
