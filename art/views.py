from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from .forms import ContactForm, SubscriberForm
from .models import Art, Artist, Contact, Subscriber

# Create your views here.
def index(request):
    return render(request, 'index.html')

def artist(request, slug):
    # lookup artist by slug
    try:
        artist = Artist.objects.get(slug__exact=slug)
        # get art
        art = Art.objects.filter(ArtistID_id=artist.ArtistID)
        return render(request, 'artist.html', {'art': art, 'artist': artist})
    except:
        # return 404
        return HttpResponseNotFound('<h1>Page Not Found</h1>')

def artists(request):
    artists = Artist.objects.all();
    return render(request, 'artists.html', {'artists': artists});

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            return render(request, 'contact.html', {'alert': 'success'})
        else:
            return render(request, 'contact.html', {'form': form, 'alert': 'fail'})
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
    
def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            Subscriber.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email
            )
            return render(request, 'subscribe.html', {'alert': 'success'})
        else:
            return render(request, 'subscribe.html', {'form': form, 'alert': 'fail'})
    else:
        form = SubscriberForm()
        return render(request, 'subscribe.html', {'form': form})


