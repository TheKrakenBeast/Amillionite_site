from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    # path('blog/', views.BlogPageView.as_view(), name='blog'),

    # about
    path('', include('About.urls')),

    # music
    path('', include('Music.urls')),

    # books (removed)
    # path('', include('Writing.urls')),

    # gigs
    path('', include('Gig.urls')),

    # news
    path('', include('News.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
