from django.db import models

# Create your models here.



# class Recipe(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     name = models.CharField(max_length=220)
#     description = models.TextField(blank=True, null=True)
#     directions = models.TextField(blank=True, null=True)
#     timestamp = models.DateTimeField(auto_now_add=True) 
#     updated = models.DateTimeField(auto_now=True) 
#     active = models.BooleanField(default=True)


# class RecipeIngredient(models.Model):
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     # recipe_id = models.AutoField -> ID to Recipe
#     name = models.CharField(max_length=220)
#     description = models.TextField(blank=True, null=True)
#     quantity = models.CharField(max_length=50, blank=True, null=True)  # 1 1/4
#     quantity_as_float = models.FloatField(blank=True, null=True)
#     # pounds, lbs, oz, gram, etc
#     unit = models.CharField(max_length=50, validators=[validate_unit_of_measure], blank=True, null=True)
#     directions = models.TextField(blank=True, null=True)
#     timestamp = models.DateTimeField(auto_now_add=True) 
#     updated = models.DateTimeField(auto_now=True) 
#     active = models.BooleanField(default=True)