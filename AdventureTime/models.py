from django.db import models
from django.contrib.auth.models import User, Group

class Capital(models.Model):
    capital = models.CharField(max_length=50)
    def __str__(self):
        return self.capital
class Language(models.Model):
    language = models.CharField(max_length=50)
    def __str__(self):
        return self.language
class Currency(models.Model):
    currency = models.CharField(max_length=3)
    def __str__(self):
        return self.currency
class Country(models.Model):
  name_country = models.CharField(max_length=60)
  desctription = models.CharField(max_length=200)
  capital_city = models.ForeignKey(Capital, on_delete=models.CASCADE)
  language = models.ForeignKey(Language, on_delete=models.CASCADE)
  currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
  def __str__(self):
      return self.name_country
class Place(models.Model):
    CATEGORY = (
        ('business','business'),
        ('nature', 'nature'),
        ('party time', 'party time'),
        ('religion', 'religion'),
        ('adventure', 'adventure'),
    )
    name_place = models.CharField(max_length=100)
    description_place = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category =models.CharField(max_length=200, null=True, choices=CATEGORY)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.name_place
#class User(User):
#     login = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=20)
#     data_birth = models.DateField()
#     def __str__(self):
#         return self.login

class Rating(models.Model):
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 7)])
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # def __str__(self):
    #    return self.rating
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment


