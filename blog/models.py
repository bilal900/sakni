from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.
class post(models.Model):
  author=models.ForeignKey(User,related_name='Post_author',on_delete=models.CASCADE)
  title=models.CharField(max_length=100)
  tags=TaggableManager()
  image=models.ImageField(upload_to='Post/')
  created_at=models.DateField(timezone.now)
  description=models.TextField(max_length=1000)
  category=models.ForeignKey('category',related_name="post_category",on_delete=models.CASCADE)
  slug=models.SlugField(null=True,blank=True) #url معمول من التايتل تبع الروم او المنتج,يعني باختصار باخد التايتل وبحذف منو المسافات وبحط بدل المسافات شخطة

     
     
  def save(self,*args,**kwargs):
      if not self.slug:
         self.slug=slugify(self.title)
         super(post,self).save(*args,**kwargs)

  def __str__(self):
       return self.title
  def get_absolute_url(self):
       return reverse('blog:post_detail', kwargs={'slug': self.slug})
   

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
       return self.name  