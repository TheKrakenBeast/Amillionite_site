from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('news/', views.news_preview, name='news-preview'),
    path('news/item/<slug:slug>', views.news_detail, name='news-detail'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


