import django_filters

from .models import *

class PlaceFilter(django_filters.FilterSet):
	class Meta:
		model = Place
		fields = '__all__'
		#exclude = [