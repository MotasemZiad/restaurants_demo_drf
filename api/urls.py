from django.urls import path, include
from views import (RestaurantsView, RestaurantDetailView,
                   RecipesView, RecipeDetailView)

urlpatterns = [
    path('restaurants/', RestaurantsView.as_view()),
    path('restaurants/<str:restaurant_id>/', RestaurantDetailView.as_view()),
    path('restaurants/<str:restaurant_id>/recipes/', RecipesView.as_view()),
    path('restaurants/<str:restaurant_id>/recipes/<str:recipe_id>/',
         RecipeDetailView.as_view()),
]
