from django.shortcuts import render

from listings.models import Listing, Band

# Create your views here.


titres = Listing.objects.all()


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_details.html', {'band': band})


def about(request):
    return render(request, 'listings/about.html')


def listing(request):
    return render(request, 'listings/listing.html', {'titres': titres})


def contact(request):
    return render(request, 'listings/contact.html')
