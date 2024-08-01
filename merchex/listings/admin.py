from django.contrib import admin

from listings.models import Band, Listing


# Register your models here.
@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'biography', 'year_formed', 'active')
    # list_editable = ('name', 'biography', 'year_formed', 'active')


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'band')
