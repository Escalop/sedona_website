from django.forms import ModelForm
from ..models.booking import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'adults', 'kids']
