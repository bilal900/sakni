from django.shortcuts import render
from property.models import Property , Place , Category
from django.db.models.query_utils import Q
from django.db.models import Count
from blog.models import post
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    places=Place.objects.all().annotate(property_count=Count('Property_place'))
    category=Category.objects.all() 
    resturant_list=Property.objects.filter(category__name='Resturant')[:5]
    hotel_list=Property.objects.filter(category__name='Hotel')[:4]
    place_list=Property.objects.filter(category__name='Places')[:3]
    recent_post=post.objects.all()[:3] 
    user_count=User.objects.all().count()
    places_count=Property.objects.filter(category__name='Places').count()
    resturant_count=Property.objects.filter(category__name='Resturant').count()
    hotel_count=Property.objects.filter(category__name='Hotel').count()

    return render(request,'settings/home.html',{
        'places' : places,
        'category':category,
        'resturant_list':resturant_list ,
        'hotel_list':hotel_list ,
        'place_list':place_list ,
        'recent_post':recent_post,
        'user_count':user_count,
        'places_count':places_count,
        'resturant_count':resturant_count,
        'hotel_count':hotel_count,
    })  


def home_search(request):
    name=request.GET.get('name')
    place=request.GET.get('place')
    
    property_list=Property.objects.filter(
        Q(name__icontains=name) &
        Q(place__name__icontains=Place)
    )
    return render(request,'settings/home_search.html',{'property_list':property_list})



def category_filter(request,category):
      category =Category.objects.get(name=category)
      property_list=Property.objects.filter(category= category)
      return render(request,'settings/home_search.html',{'property_list':property_list})


def contect_us(request):
    pass      

