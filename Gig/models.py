from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")


class Gig(models.Model):
    date = models.DateField(blank=False, default=None, validators=[validate_date])
    venue = models.CharField(max_length=100, blank=False, default="TBA")
    supports = models.TextField(blank=True, null=True, max_length=500)
    time = models.TimeField()
    url = models.URLField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.venue





