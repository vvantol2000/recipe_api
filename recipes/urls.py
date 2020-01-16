from django.urls import path, re_path, include

from recipes.views import recipes_list, recipes_detail, RecipeList, RecipeDetail, RecipeApiList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('recipes-api', RecipeApiList)

urlpatterns = [
    path('', include(router.urls)),
    path('recipe/', RecipeList.as_view(), name='recipe_list'),
    path('recipe-list/', recipes_list, name='recipes_list'),
    path('recipe/<int:pk>', RecipeDetail.as_view(), name='recipe_detail')
]