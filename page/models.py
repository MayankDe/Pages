from django.db import models

# Create your models here.
class ContactUs(models.Model):
    Name=models.CharField(max_length=150)
    Email =models.EmailField(max_length=300)

    Address=models.CharField(max_length=500)
    Message = models.TextField()
    Timestamp= models.DateTimeField(auto_now_add=True, blank=True)

class Post(models.Model):
    Strength = models.TextField()
    Weakness = models.TextField()
    Timestamp= models.DateTimeField(auto_now_add=True, blank=True)
