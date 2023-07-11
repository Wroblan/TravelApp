from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView, DeleteView, FormView
from AdventureTime import models
from AdventureTime import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

def hello(request):
  return HttpResponse('Hello, world!')

class CountryReadView(View):
  def get(self, request):
      return render(request, template_name='country_read.html', context={'dane': models.Country.objects.all()})

class CountryCreateView(LoginRequiredMixin, FormView):
    success_url = reverse_lazy('country_read')
    form_class = forms.CountryForm
    model = models.Country
    template_name = 'country_create.html'
    login_url = "login"
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
class CountryUpdateView(LoginRequiredMixin, UpdateView):
    success_url = reverse_lazy('country_read')
    form_class = forms.CountryForm
    model = models.Country
    template_name = 'country_create.html'
    login_url = "login"
class CountryDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('country_read')
    model = models.Country
    template_name = 'country_delete.html'
    login_url = "login"

class PlaceReadView(View):
  def get(self, request):
      return render(request, template_name='place_read.html', context={'dane': models.Place.objects.all()})

class PlaceCreateView(LoginRequiredMixin, FormView):
    success_url = reverse_lazy('place_read')
    form_class = forms.PlaceForm
    model = models.Place
    template_name = 'place_create.html'
    login_url = "login"
    def form_valid(self, form):
        result = super().form_valid(form)
        models.Place.objects.create(
            name_place=form.cleaned_data['name_place'],
            description_place=form.cleaned_data['description_place'],
            country=form.cleaned_data['country'],

        )
        return result

class UserCreateView(CreateView):
    template_name = 'RegisterView.html'
    form_class = UserCreationForm
    model = models.User
    success_url = reverse_lazy('user_read')

def search_view(request):
    form = forms.SearchForm()
    results = []
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            place = form.cleaned_data['place']
            country = form.cleaned_data['country']
            category = form.cleaned_data['category']
            if place:
                places = models.Place.objects.filter(name_place__icontains=place)
            if country:
                places = models.Place.objects.filter(country__name_country__icontains=country)
            if category:
                places = models.Place.objects.filter(category__icontains=category)
            results = places
    return render(request, 'SearchView.html', {'form': form, 'results': results})

@login_required(login_url='login')
def like_place(request, place_id):
    place = get_object_or_404(models.Place, pk=place_id)
    place.likes += 1
    place.save()
    return HttpResponse('Like!')

class Rating(LoginRequiredMixin, FormView):
    success_url = reverse_lazy('place_read')
    form_class = forms.RatingForm
    model = models.Rating
    template_name = 'place_create.html'
    login_url = "login"
    def form_valid(self, form):
        result = super().form_valid(form)
        models.Rating.objects.create(
            rating=form.cleaned_data['rating'],
            user=self.request.user,
            place=models.Place.objects.get(pk=self.kwargs.get('place_id')),
            #---> In a class-based view, all of the elements from the URL are placed into self.args (if they're non-named groups)
            # or self.kwargs (for named groups) --> self.kwargs['pk'].

        )
        return result

class Comment(LoginRequiredMixin, FormView):
    success_url = reverse_lazy('place_read')
    form_class = forms.CommentForm
    model = models.Comment
    template_name = 'place_create.html'
    login_url = "login"
    def form_valid(self, form):
        result = super().form_valid(form)
        models.Comment.objects.create(
            comment=form.cleaned_data['comment'],
            user=self.request.user,
            place=models.Place.objects.get(pk=self.kwargs.get('place_id')),
        )
        return result

