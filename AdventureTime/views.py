from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView, DeleteView
from AdventureTime import models
from AdventureTime import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

def hello(request):
  return HttpResponse('Hello, world!')

class CountryReadView(View):
  def get(self, request):
      return render(request, template_name='country_read.html', context={'dane': models.Country.objects.all()})

class CountryCreateView(CreateView):
    success_url = reverse_lazy('country_read')
    form_class = forms.CountryForm
    model = models.Country
    template_name = 'country_create.html'
    def form_valid(self, form):
        result = super().form_valid(form)
        models.Country.objects.create(
            name_country=form.cleaned_data['name_country'],
            desctription=form.cleaned_data['desctription'],
            capital_city=form.cleaned_data['capital_city'],
            language=form.cleaned_data['language'],
            currency=form.cleaned_data['currency'],

        )
        return result
class CountryUpdateView(UpdateView):
    success_url = reverse_lazy('country_read')
    form_class = forms.CountryForm
    model = models.Country
    template_name = 'country_create.html'
class CountryDeleteView(DeleteView):
    success_url = reverse_lazy('country_read')
    model = models.Country
    template_name = 'country_delete.html'

class PlaceReadView(View):
  def get(self, request):
      return render(request, template_name='place_read.html', context={'dane': models.Place.objects.all()})

class PlaceCreateView(CreateView):
    success_url = reverse_lazy('place_read')
    form_class = forms.PlaceForm
    model = models.Place
    template_name = 'place_create.html'
    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     models.Place.objects.create(
    #         name_place=form.cleaned_data['name_place'],
    #         description_place=form.cleaned_data['description_place'],
    #         country=form.cleaned_data['country'],
    #
    #     )
    #     return result

class UserCreateView(CreateView):
    template_name = 'RegisterView.html'
    form_class = UserCreationForm
    model = models.User
    success_url = reverse_lazy('user_read')