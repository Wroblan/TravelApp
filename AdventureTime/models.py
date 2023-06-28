from django.db import models

class Capital(models.Model):
    capital = models.CharField(max_length=50)
class Language(models.Model):
    language = models.CharField(max_length=50)
class Currency(models.Model):
    currency = models.CharField(max_length=3)
class Country(models.Model):
  name_country = models.CharField(max_length=60)
  desctription = models.CharField(max_length=200)
  capital_city = models.ForeignKey(Capital, on_delete=models.CASCADE)
  language = models.ForeignKey(Language, on_delete=models.CASCADE)
  currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
class Place(models.Model):
    name_place = models.CharField(max_length=100)
    description_place = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
class User(models.Model):
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    data_birth = models.DateField()
class Category(models.Model):
    category = models.CharField(max_length=30)
class Rating(models.Model):
    rating = models.IntegerField(max_length=6)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)


