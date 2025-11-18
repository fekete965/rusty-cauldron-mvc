from django.db import models
from django.utils import timezone

from tables.users import User


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    title = models.CharField(max_length=100)
    prep_time = models.IntegerField(null=True, blank=True)
    cooking_time = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "recipes"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
