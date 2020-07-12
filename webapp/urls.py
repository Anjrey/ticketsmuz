from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register-band/', views.register_band, name='register-band'),
    path('events/', views.events, name='events'),
    path('bands/', views.bands, name='bands'),
    path('bands/<int:pk>/', views.band_page, name='band-page'),
    path('fan/<int:pk>/', views.fan_page, name='fan-page')
]