from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name='home'),
path('about',views.about,name='about'),
path('services',views.services,name='services'),
path('contact',views.contact,name='contact'),
path('add',views.add,name='add'),
path('offers',views.offers,name='offers'),
]
