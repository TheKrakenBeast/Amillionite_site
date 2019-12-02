from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class BlogPageView(TemplateView):
    template_name = 'pages/news.html'


class WritingPageView(TemplateView):
    template_name = 'pages/works.html'


class GigsPageView(TemplateView):
    template_name = 'pages/gigs.html'
