"""
URL configuration for rustyCauldron project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LogoutView
from main.views import (
    AddRecipe, DeleteRecipe, IndexPageView, LoginPageView, MyRecipesPageView,
    NotFoundPageView, RecipePageView, RecipesPageView, SignupPageView, UpdateRecipe
)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', IndexPageView.as_view(), name='index'),
    path('add-recipe/', AddRecipe.as_view(), name='add-recipes'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('my-recipes/', MyRecipesPageView.as_view(), name='my-recipes'),
    path('not-found-page/', NotFoundPageView.as_view(), name='not-found-page'),
    path('recipe/<int:recipe_id>/', RecipePageView.as_view(), name='recipe'),
    path('recipes/<int:recipe_id>/delete/', DeleteRecipe.as_view(), name='delete-recipe'),
    path('recipes/<int:recipe_id>/update/', UpdateRecipe.as_view(), name='update-recipe'),
    path('recipes/', RecipesPageView.as_view(), name='recipes'),
    path('signup/', SignupPageView.as_view(), name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
