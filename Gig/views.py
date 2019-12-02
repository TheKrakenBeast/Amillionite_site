from django.shortcuts import render
from .models import Gig
from datetime import date


def gig_date(request):
    gig = Gig.objects.all().filter(date__gte=date.today()).order_by('date')
    return render(request, 'pages/gigs.html', {'gig': gig})

