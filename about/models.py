from django.db import models

# Create your models here.
class About(models.Model):
    what_we_do=models.CharField(max_length=600)
    our_mission=models.CharField(max_length=600)
    our_goals=models.CharField(max_length=600)
    image=models.ImageField(upload_to='about/')


    def __str__(self):
        return str(self.id)

class FAQ(models.Model):
    title=models.CharField(max_length=600)
    description=models.CharField(max_length=600)

    def __str__(self):
        return self.title        
