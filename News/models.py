from django.core.validators import FileExtensionValidator
from django.db import models
from autoslug import AutoSlugField


class NewsItem(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default="Amillionite")
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=True, blank=True)
    slug = AutoSlugField(populate_from='title')
    videoEmbed = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/',
                              validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp'])],
                              null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.text[:500] + '...'
