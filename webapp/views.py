from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import BandRegistrationForm


def home(request):
    pagetitle = 'Homepage'

    return render(request, 'webapp/home.html', {'pagetitle': pagetitle})


def events(request):
    pagetitle = 'Events Board'

    return render(request, 'webapp/events_board.html', {'pagetitle': pagetitle})


def register_band(request):
    pagetitle = 'New Band Registration'

    form = BandRegistrationForm()
    if request.method == 'POST':
        form = BandRegistrationForm(request.post)
        if form.is_valid:
            form.save()
            return redirect('events')

    args = {
        'form': form,
        'pagetitle': pagetitle
    }

    return render(request, 'webapp/register_band.html', args)


def bands(request):
    pagetitle = 'Bands'

    bands = Band.objects.all()
    amount = Band.objects.count()
    args = {
        'bands': bands,
        'amount': amount,
        'pagetitle': pagetitle
    }

    return render(request, 'webapp/bands.html', args)


def band_page(request, pk):
    band = Band.objects.get(id=pk)
    pagetitle = band.name + ' Page'
    args = {
        'band': band,
        'pagetitle': pagetitle
    }
    return render(request, 'webapp/band_page.html', args)


def fan_page(request, pk):
    fan = Fan.objects.get(id=pk)
    pagetitle = fan.name + ' page'
    args = {
        'pagetitle': pagetitle
    }

    return render(request, 'webapp/fan-page.html', args)