from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, CreateView, UpdateView, DeleteView
from AdventureTime import models


def hello(request):
  return HttpResponse('Hello, world!')

class CountryReadView(View):
  def get(self, request):
      return render(request, template_name='country_read.html', context={'dane': models.Country.objects.all()})