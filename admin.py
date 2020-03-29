from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin


admin.site.register(Article)
admin.site.register(Announcement)
admin.site.register(Video)
admin.site.register(VideoYear)
admin.site.register(ArticleStatistic)
admin.site.register(TopicYear)



class PhotoInline(admin.TabularInline):
    fieldsets = [
        ('Upload Image', {'fields': ['image']})
    ]
    model = Photo
    extra = 3

class TopicYearAdmin(admin.ModelAdmin):
    fieldsets =[(None, {'fields': ['year']}),]


class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Basic Info', {'fields': ['description']}),
        (None, {'fields': ['year']}),

    ]
    inlines = [PhotoInline]
admin.site.register(Topic, TopicAdmin)

class VideoAdmin(admin.ModelAdmin):
    field =['title','post','video','year']

class VideoYearAdmin(admin.ModelAdmin):
    field =['year']

class ArticleAdmin(admin.ModelAdmin):
    field =['title','post','date','image','slug']


class AnnouncementAdmin(admin.ModelAdmin):
    field =['title','post','image', 'date']

class VideoAdmin(AdminVideoMixin,admin.ModelAdmin):
    field =['title','year','post','video']

class ArticleStatisticAdmin(admin.ModelAdmin):
     list_display = ('__str__', 'date', 'views')  # отображаемые поля в админке
     search_fields = ('__str__', )                # поле, по которому производится поиск
