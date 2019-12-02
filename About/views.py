from django.shortcuts import render
from .models import About


def about_section(request):
    about = About.objects.latest('date_added')
    return render(request, 'pages/about.html', {'about': about})
