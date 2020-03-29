from .models import *
from django.urls import path, include
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.mail import send_mail
from .forms import ContactForm
from django.db.models import Sum
from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import TruncYear
import django_filters
from django.views.generic import ListView, DetailView




def barolo (request):
    return render (request, 'sensory_analysis/barolo.html')

def burgundy (request):
    return render (request, 'sensory_analysis/Burgundy.html')

def barbaresco (request):
    return render (request, 'sensory_analysis/Barbaresco.html')


def articles_list (request):
    articles = Article.objects.all()
    announcements = Announcement.objects.all()
    return render(request, 'sensory_analysis/index.html', context={'articles': articles , 'announcements': announcements})


def video_list(request):
    yyitems = Video.objects.all()
    if request.GET.get('year', None) is not None:
        yyitems = yyitems.filter(year__year=request.GET.get('year'))
    years = TopicYear.objects.all()
    return render(request,'sensory_analysis/videoGallery.html',context={'yyitems':yyitems,'years':years})
    

def about_us (request):
    return render (request, 'sensory_analysis/about.html')

def photogallery(request):
    topics = Topic.objects.all()
    if request.GET.get('year', None) is not None:
        topics = topics.filter(year__year=request.GET.get('year'))
    years = TopicYear.objects.all()
    return render (request, 'sensory_analysis/photoGallery.html', context={'topics':topics, 'years':years})

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    return render(request, 'sensory_analysis/photos.html', context={'topic': topic})


def contacts(request):
    return render(request, 'sensory_analysis/contacts.html')



def page_contact(request):
    sent = False


    mailfrom = settings.EMAIL_HOST_USER
    mailto = [settings.EMAIL_HOST_USER]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'Autister - Новое письмо от {}'.format(cd['name'],cd['job'],)
            message = 'Прислал {}. Пишет: {}'.format(cd['tel'],cd['email'], cd['message'])
            send_mail(subject, message, mailfrom, mailto)
            sent = True
    else:
        form = ContactForm()
    return render(request, 'sensory_analysis/page_contact.html', {'form': form, 'sent': sent})


class EArticleView(View):
    template_name = 'sensory_analysis/index.html'

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=self.kwargs['article_id'])
        context = {}
        # Далее забираем объект сегодняшней статистики или создаём новый, если требуется
        obj, created = ArticleStatistic.objects.get_or_create(
            defaults={
                "article": article,
                "date": timezone.now()
            },
            # При этом определяем, забор объекта статистики или его создание
            # по двум полям: дата и внешний ключ на статью
            date=timezone.now(), article=article
        )
        obj.views += 1    # инкрементируем счётчик просмотров и обновляем поле в базе данных
        obj.save(update_fields=['views'])

        # А теперь забираем список 5 последний самых популярных статей за неделю
        popular = ArticleStatistic.objects.filter(
            # отфильтровываем записи за последние 7 дней
            date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]
        ).values(
            # Забираем интересующие нас поля, а именно id и заголовок
            # К сожалению забрать объект по внешнему ключу в данном случае не получится
            # Только конкретные поля из объекта
            'article_id', 'article_title', 'article_views',
        ).annotate(
            # Суммируем записи по просмотрам
            # Всё суммируется корректно с соответствием по запрашиваемым полям объектов
            views=Sum('views')
        ).order_by(
            # отсортируем записи по убыванию
            '-views')[:5]  # Заберём последние пять записей
        context['popular_list'] = popular # Отправим в контекст список статей
        return render_to_response(template_name=self.template_name, context=context)


def wines(request):
    return render (request, 'sensory_analysis/wines.html')

def white_whine(request):
    return render (request, 'sensory_analysis/white-whine.html')

def red_wine(request):
    return render (request, 'sensory_analysis/red-wine.html')


def educational_program(request):
    return render (request, 'sensory_analysis/educational-program.html')

def training(request):
    return render (request, 'sensory_analysis/training.html')
