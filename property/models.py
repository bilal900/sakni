from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
class Property(models.Model):
     name=models.CharField(max_length=100)
     image=models.ImageField(upload_to='Property')
     price=models.IntegerField(default=0)   
     description=models.TextField(max_length=10000)
     place=models.ForeignKey('Place',related_name='Property_place',on_delete=models.CASCADE)
     category=models.ForeignKey('category',related_name='Property_category',on_delete=models.CASCADE)
     created_at=models.DateTimeField(default=timezone.now)
     slug=models.SlugField(null=True,blank=True) #url معمول من التايتل تبع الروم او المنتج,يعني باختصار باخد التايتل وبحذف منو المسافات وبحط بدل المسافات شخطة

     
     
     def save(self,*args,**kwargs):
       if not self.slug:
         self.slug=slugify(self.name)
         super(Property,self).save(*args,**kwargs)
     def __str__(self): 
        return self.name    
     def get_absolute_url(self):
         return reverse('property:property_detail', kwargs={'slug': self.slug})
    


class PropertyImages(models.Model):
    Property=models.ForeignKey('Property',related_name='Property_image',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Propertyimages/')
    def __str__(self):
        return str(self.Property)

class Place(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='Places/')
   
    def __str__(self):
        return self.name
  
class Category(models.Model): 
   name=models.CharField(max_length=100)
   icon=models.CharField(max_length=200)
   def __str__(self):
        return self.name

class PropertyReview(models.Model):
    author=models.ForeignKey(User,related_name='review_author',on_delete=models.CASCADE)
    property=models.ForeignKey('Property',related_name='Review_Property',on_delete=models.CASCADE)    
    rate=models.IntegerField(default=0)
    feedback=models.TextField(max_length=2000)
    created_at=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.property) 

COUNT=(
    (1,1),
    (2,2),
    (3,3),
    (4,4),
)
class proberty_book(models.Model):
    user=models.ForeignKey(User,related_name='book_owner',on_delete=models.CASCADE)
    property=models.ForeignKey('Property',related_name='book_Property',on_delete=models.CASCADE)  
    date_from=models.DateField(default=timezone.now)
    date_to=models.DateField(default=timezone.now)
    guest=models.IntegerField(choices=COUNT)
    children=models.IntegerField(choices=COUNT)

    def __str__(self) :
        return str(self.property)
        



