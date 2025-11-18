from django.db import models
from django.utils import timezone

from tables.recipes import Recipe


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    measurement = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ingredients"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.amount} {self.measurement}"
