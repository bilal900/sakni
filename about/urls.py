from django.urls import path
from . views import AboutVeiw
app_name='abot'

urlpatterns = [
    path('',AboutVeiw.as_view(),name='about')
]
