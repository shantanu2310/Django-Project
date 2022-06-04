from django.urls import path
from . import views

urlpatterns = [
    path('isauth', views.isauth, name='isauth'),
    path('inquiry', views.inquiry, name='inquiry'),
]
