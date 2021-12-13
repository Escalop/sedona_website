from django.http import HttpResponse
from django.shortcuts import render
#from ..forms.sort_and_filter import HotelSortForm, BooleanFildForm
from ..models.hotel_page import HotelPage
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView


class HotelList(ListView):
        model = HotelPage
        query = HotelPage.objects.all()
        template_name = 'pages/hotels_list.html'
        context_object_name = 'posts'
        allow_empty = False

'''def hotel_list(request):
    hotels = HotelPage.objects.all()
    form = HotelSortForm(request.GET)

    if form.is_valid():
        if form.cleaned_data["min_price"]:
            hotels = hotels.filter(price_gte=form.cleaned_data["min_price"])

        if form.cleaned_data["max_price"]:
            hotels = hotels.filter(price_lte=form.cleaned_data["max_price"])

        if form.cleaned_data["ordering"]:
            hotels = hotels.order_by(price_lte=form.cleaned_data["ordering"])

    return  render(request, 'pages/post_list.html', {"hotels": hotels, "form": form})'''
'''from django.views.generic import ListView

from ..models import HotelPage
from ..forms import HotelSortForm


class SearchResultView(ListView):
    form_class = HotelSortForm
    template_name = 'pages/post_list.html'
'''

"""model = HotelPage
    query = HotelPage.objects.all()
    template_name = 'pages/post_list.html'
    motels = HotelPage.objects.filter(type__icontains='МОТЕЛЬ')
    hotel = HotelPage.objects.filter(type__contains='тиница')"""

'''def some_function(request,hotels):
    if request.GET:
        print(request.GET)'''

'''def formviewdata(req):
    form = BooleanFildForm()
    print('Data from FORM', req.GET)
    return render(req, 'post_list.html', {'FORM': form})'''