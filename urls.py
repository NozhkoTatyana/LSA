from django.urls import path
from .views import *
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from django.conf import settings
from . import views




urlpatterns = [

    path('', articles_list, name='articles_list'),
    path('video_list/', video_list, name='video_list'),
    path('about_us', about_us, name='about_us'),
    path('contacts', contacts, name='contacts'),
    path('tinymce/', include('tinymce.urls')),
    path('<article_id>[0-9]+)', views.EArticleView.as_view(), name='article'),
    path('wines/', wines, name='wines'),
    path('white_whine/', white_whine, name='white_whine'),
    path('red_wine/', red_wine, name='red_wine'),
    path('red_wine/barolo', views.barolo, name='barolo'),
    path('red_wine/burgundy', views.burgundy, name='burgundy'),
    path('red_wine/barbaresco', views.barbaresco, name='barbaresco'),
    path('photoGallery/', views.photogallery, name='photoGallery'),
    path('feedback/', views.page_contact, name='page_contact'),
    path('photoGallery/<int:topic_id>', views.topic, name='topic'),
    path('educational_program', views.educational_program, name='educational_program'),
    path('training', views.training, name='training'),
    #path('topic_year/', views.topic_year, name='year'),





]
