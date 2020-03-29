from django.db import models
from embed_video.fields import EmbedVideoField
from django.utils import timezone
from tinymce.models import HTMLField
from datetime import datetime
from django.utils.timezone import now

class TopicYear(models.Model):
    year = models.CharField(max_length=4)


    def __str__(self):
        return self.year

    class Meta:
        ordering = ['-year']


class Topic(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    year = models.ManyToManyField(TopicYear, related_name="topic_year")


    def __str__(self):
        return self.name





class Photo(models.Model):
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photo_folder')




def photo_folder(instance,filename):
    return "{}/{}".format('photo',translit(filename,'ru',reversed=True))


def upload_article_images_folder(instance,filename):
    filename=+filename.split('.')[-1]
    return "{}/{}".format(instance, filename)

def video_folder(instance,filename):
    return "{}/{}".format('video',translit(filename,'ru',reversed=True))


class Article(models.Model):
    title = models.CharField(max_length = 150, db_index=True)
    post = HTMLField(blank=True,db_index=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='article_images_folder', blank=True)
    pdf = models.URLField(max_length = 150, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

class Announcement(models.Model):
    title = models.CharField(max_length = 150, db_index=True)
    post = HTMLField(blank=True,db_index=True)
    image = models.ImageField(upload_to='announcement_images_folder',blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
            ordering = ['-date']

class VideoYear(models.Model):
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.year

class Video(models.Model):

    title = models.CharField(max_length = 120, db_index=True)
    video = models.FileField(upload_to='video_folder',db_index=True, blank=False)
    post =  models.TextField(blank=True,db_index=True)
    year = models.ManyToManyField(VideoYear, related_name="video_year")
    #publication_year = models.IntegerField(db_index=True)

    def __str__(self):
        return self.title


class ArticleStatistic(models.Model):
    class Meta:
        db_table = "ArticleStatistic"

    article = models.ForeignKey(Article,on_delete = models.CASCADE)
    date = models.DateField('Дата', default=timezone.now)
    views = models.IntegerField('Просмотры', default=0)

    def __str__(self):
        return self.article.title
