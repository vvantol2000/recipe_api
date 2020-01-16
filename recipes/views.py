from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from recipes.models import Recipe
from rest_framework import viewsets
from .serializers import RecipeSerializer

# Create your views here.


class RecipeList(ListView):
    model = Recipe


class RecipeDetail(DetailView):
    model = Recipe


class RecipeApiList(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


def recipes_list(request):
    recipes = Recipe.objects.all()
    data = {"results": list(recipes.values("title"))}
    return JsonResponse(data)


def recipes_detail(request, pk):
    pass