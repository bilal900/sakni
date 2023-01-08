from django.db import models

# 
# Create your models here.
class Settings(models.Model):
    site_name=models.CharField(max_length=60)
    logo=models.ImageField(upload_to='settings/')
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    description=models.TextField(max_length=200)
    fb_link=models.URLField(max_length=500)
    instagram_link=models.URLField(max_length=500)
    twitter_link=models.URLField(max_length=500)
    adress=models.CharField(max_length=100)
    
    def __str__(self):
        return self.site_name