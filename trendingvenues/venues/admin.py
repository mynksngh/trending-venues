# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from venues.models import City, State, Locality

# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', )
    # list_filter = (
    #     ('country', admin.RelatedOnlyFieldListFilter),
    # )

class StateAdmin(admin.ModelAdmin):
    list_display = ('name', )
    # list_filter = (
    #     ('country', admin.RelatedOnlyFieldListFilter),
    # )


class LocalityAdmin(admin.ModelAdmin):
	list_display = ('name', )
		


admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Locality, LocalityAdmin)
