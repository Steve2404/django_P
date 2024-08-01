from django.shortcuts import render

from listings.models import Listing, Band

# Create your views here.

bands = Band.objects.all()
titres = Listing.objects.all()
# comb = zip(bands, titres)


def hello(request):
    return render(request, 'listings/hello.html', {'bands': bands, 'comb': 'comb'})


def about(request):
    return render(request, 'listings/about.html')


def listing(request):
    return render(request, 'listings/listing.html', {'titres': titres})


def contact(request):
    return render(request, 'listings/contact.html')
