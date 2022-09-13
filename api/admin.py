from django.contrib import admin
from .models import (Restaurant, Recipe, Ingredient)
# Register your models here.


admin.site.register(Restaurant)
admin.site.register(Recipe)
admin.site.register(Ingredient)
