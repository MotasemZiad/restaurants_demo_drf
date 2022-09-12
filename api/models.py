from django.db import models
import uuid
# Create your models here.

recipe_types = [('BREAKFAST', 'Breakfast'), ('LUNCH', 'Lunch'),
                ('COFFEE', 'Coffee'), ('DINNER', 'Dinner')]


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")
    address = models.CharField(
        max_length=120, null=True, verbose_name="Address")
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")
    type = models.CharField(max_length=20, choices=recipe_types)
    thumbnail = models.ImageField(
        upload_to="recipe_thumbnails", default="recipe_thumbnails/default.png")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, verbose_name="Name")
    recipe = models.ManyToManyField(Recipe)

    def __str__(self):
        self.name
