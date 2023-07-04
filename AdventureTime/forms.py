from django import forms

from AdventureTime import models


class CountryForm(forms.ModelForm):
    class Meta:
        model = models.Country
        fields = '__all__'

class PlaceForm(forms.ModelForm):
    class Meta:
        model = models.Place
        fields = '__all__'