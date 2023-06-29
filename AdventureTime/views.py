from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView, DeleteView
from AdventureTime import models
from AdventureTime import forms

def hello(request):
  return HttpResponse('Hello, world!')

class CountryReadView(View):
  def get(self, request):
      return render(request, template_name='country_read.html', context={'dane': models.Country.objects.all()})

class CountryCreateView(CreateView):
    success_url = reverse_lazy('country-read')
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
