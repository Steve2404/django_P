from django.core.mail import send_mail
from django.shortcuts import render, redirect

from listings.forms import ContactUsForm, BandForm, ListingForm
from listings.models import Listing, Band


# Create your views here.

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_details.html', {'band': band})


def about(request):
    return render(request, 'listings/about.html')


def listing_list(request):
    titres = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'titres': titres})


def listing_detail(request, listing_id):
    titre = Listing.objects.get(id=listing_id)
    return render(request, 'listings/listing_details.html', {'titre': titre})


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band_detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"Message from {form.cleaned_data['name'] or 'anonyme'} via MerchEx contact Us Form",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect("Send Email ...")
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html',
                  {'form': form})


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing_detail', listing.id)
    else:
        form = ListingForm()
        return render(request, 'listings/listing_create.html', {'form': form})


def band_update(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band_detail', band.id)
    else:
        form = BandForm(instance=band)
        return render(request, 'listings/band_update.html', {'form': form})


def listing_update(request, listing_id):
    ls = Listing.objects.get(id=listing_id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=ls)
        if form.is_valid():
            form.save()
            return redirect('listing_detail', ls.id)
    else:
        form = ListingForm(instance=ls)
        return render(request, 'listings/listing_update.html', {'form': form})


def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        band.delete()
        return redirect('band_list')
    return render(request, 'listings/bansd_delete.html', {'band': band})


def listing_delete(request, listing_id):
    liste = Listing.objects.get(id=listing_id)
    if request.method == 'POST':
        liste.delete()
        return redirect('listing_list')

    return render(request, 'listings/listing_delete.html',
                  {'liste': liste})
