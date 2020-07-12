from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    GENRE = (
        ('Rap', 'Rap'),
        ('Pop', 'Pop'),
        ('Metal', 'Metal'),
        ('PostHardCore', 'PostHardCore'),
        ('Melodic Metalcore', 'Melodic Metalcore')
    )

    CITIES = (
        ('Kiev', 'Kiev'),
        ('Lviv', 'Lviv'),
        ('Dnipro', 'Dnipro')
    )

    name = models.CharField(max_length=150, blank=False)
    genre = models.CharField(max_length=200, choices=GENRE)
    logo = models.CharField(max_length=1000, default='Band Logo place')
    city = models.CharField(max_length=25, choices=CITIES, default='city', blank=False)
    description = models.CharField(max_length=1500, default='Description here')
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name



class Event(models.Model):
    CITIES = (
        ('Kiev', 'Kiev'),
        ('Lviv', 'Lviv'),
        ('Dnipro', 'Dnipro')
    )

    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=1500)
    city = models.CharField(max_length=25, choices=CITIES, default='city')
    date_and_time = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.band.name + ' : ' + self.title


class Fan(models.Model):
    name = models.CharField(max_length=100, blank=False)
    event = models.ManyToManyField(Event, blank=True)
    email = models.EmailField(max_length=100, default='email here', blank=False)
    description = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return self.name
