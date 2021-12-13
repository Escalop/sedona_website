from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from ..models import HotelPage

'''
TIPE_OF_HOUSING = ['ГОСТИНИЦА', 'мотель', 'АПАРТАМЕНТЫ']

class BooleanFildForm(forms.Form):
    Checkboxinput = forms.BooleanField()

class HotelSortForm(ModelForm):
   # min_price = forms.IntegerField(label="from", required=False)
   # max_price = forms.IntegerField(label="to", required=False)
    tipe_of_housing = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=TIPE_OF_HOUSING,)

    class Meta:
        model = HotelPage
        fields = [ 'type', 'title']'''
'''widgets = {
            'type': forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=TIPE_OF_HOUSING,),
        }'''

'''ordering = forms.ChoiceField(label="sortirovka", required=False, choices=[
        ["type",""],
        ["price", "cheap first"],
        ["-price", "expensive first"],
        ["rating", "big first"],
    ])'''

