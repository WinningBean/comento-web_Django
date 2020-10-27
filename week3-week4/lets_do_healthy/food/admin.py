from django.contrib import admin
from .models import Food, NutritionFacts

admin.site.register(Food)
admin.site.register(NutritionFacts)