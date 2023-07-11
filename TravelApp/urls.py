"""TravelApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AdventureTime import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', views.UserCreateView.as_view(), name="user_read"),
    path('hello/', views.hello),
    path('country/read', views.CountryReadView.as_view(), name='country_read'),
    path('country/create', views.CountryCreateView.as_view(), name='country-create'),
    path('country-update/<pk>', views.CountryUpdateView.as_view(), name="country_update"),
    path('country-delete/<pk>', views.CountryDeleteView.as_view(), name="country_delete"),
    path('place/read', views.PlaceReadView.as_view(), name='place_read'),
    path('place/create', views.PlaceCreateView.as_view(), name='place-create'),
    path('place/search', views.search_view, name='place-search'),
    path('place/<int:place_id>/like/', views.like_place, name='like_place'),
    path('rating/<int:place_id>', views.Rating.as_view(), name='rating'),
    path('comment/<int:place_id>', views.Comment.as_view(), name='comment'),

]
