from rest_framework import serializers
from .models import (Restaurant, Recipe, Ingredient)
import base64
from django.conf import settings
import os


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone']


class RecipeSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField('encode_thumbnail')
    ingredients = serializers.SerializerMethodField('get_ingredients')

    def encode_thumbnail(self, recipe):
        with open(os.path.join(settings.MEDIA_ROOT, recipe.thumbnail.name), "rb") as image_file:
            return base64.b64encode(image_file.read())

    def get_ingredients(self, recipe):
        try:
            recipe_ingredients = Ingredient.objects.filter(id=recipe.id)
            return IngredientSerializer(recipe_ingredients, many=True).data
        except Ingredient.DoesNotExist:
            return None

    def create(self, validated_data):
        ingredients_data = validated_data.pop("ingredient")
        restaurant = Restaurant.objects.get(pk=validated_data['restaurant_id'])
        validated_data["restaurant"] = restaurant
        recipe = Recipe.objects.create(**validated_data)

        if ingredients_data:
            for ingredient_dict in ingredients_data:
                ingredient = Ingredient(name=ingredient_dict['name'])
                ingredient.save()
                ingredient.recipe.add(recipe)
        return recipe

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'type', 'thumbnail', 'ingredients']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']
