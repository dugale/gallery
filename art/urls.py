from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artists/<slug>', views.artist, name='artist'),
    path('artists', views.artists, name='artists'),
    path('contact', views.contact, name='contact'),
    path('subscribe', views.subscribe, name='subscribe')
]
