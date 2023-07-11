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

class SearchForm(forms.Form):
    place = forms.CharField(label='Place', max_length=100,required=False)
    country = forms.CharField(label='Country', max_length=100, required=False)
    category = forms.CharField(label='Category', max_length=100, required=False)

class RatingForm(forms.ModelForm):
    #name_place = forms.ModelChoiceField(queryset=models.Place.objects.values_list('name_place'))
    # rating = forms.IntegerField(label='Rating', min_value=1, max_value=6, required=False)
    class Meta:
        model = models.Rating
        fields = ['rating']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['comment']