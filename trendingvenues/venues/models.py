# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class State(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	is_active = models.BooleanField(default=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'states'

class City(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	state = models.ForeignKey(State, null=True,  blank=True)
	is_active = models.BooleanField(default=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'cities'


class Locality(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	city = models.ForeignKey(City, null=True,  blank=True)
	pincode = models.CharField(max_length=6, null=True, blank=True)
	is_active = models.BooleanField(default=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'localities'


class FoodCategory(object):
	VEG = 0
    NONVEG = 1
    EGG = 2
		

class Venues(models.Model):
	FOOD_CATEGORY_CHOICES = (
        (VEG, 'Vegetarian'),
        (NONVEG, 'Non-Vegetarian'),
        (EGG, 'Egg'),
    )
    food_catego = models.CharField(
        max_length=1,
        choices=FOOD_CATEGORY_CHOICES,
        default=VEG,
    )
	name= models.CharField(max_length=255, null=True, blank=True)
	city = models.ForeignKey(City, null=True,  blank=True)
	locality = models.ForeignKey(Locality, null=True,  blank=True)
	address = models.CharField(max_length=255, null=True, blank=True)
	min_capacity = models.CharField(max_length=10, null=True, blank=True, default=0)
	max_capacity = models.CharField(max_length=10, null=True, blank=True, default=0)
	facebook_url = models.CharField(max_length=255, null=True, blank=True)
	twitter_url = models.CharField(max_length=255, null=True, blank=True)
	google_place_url = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'venues'