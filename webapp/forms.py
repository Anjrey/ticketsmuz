from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Band, Fan, Event


class BandRegistrationForm(UserCreationForm):
    class Meta:
        model = Band
        fields = [
            'name',
            'city',
            'email'
        ]
