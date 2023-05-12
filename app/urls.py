from django.urls import path, include
from django import urls
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.helloWorld, name='Hello'),
    path('s3_images/', views.s3_images, name='s3_images'),
    path('AzureTranslate/', views.AzureTranslate, name='AzureTranslate'),
    
]