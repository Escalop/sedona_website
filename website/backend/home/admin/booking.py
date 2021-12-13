from django.contrib import admin
from ..models.booking import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('check_in', 'check_out', 'adults', 'kids')
