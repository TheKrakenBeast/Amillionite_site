from django.shortcuts import render
from .models import NewsItem


def news_preview(request):
    news_items = NewsItem.objects.all().order_by('-date_added')
    return render(request, 'pages/news-preview.html', {'news_items': news_items})


def news_detail(request, slug):
    # return HttpResponse(slug)
    news_item = NewsItem.objects.get(slug=slug)
    return render(request, 'pages/news.html', {'news_item': news_item})

