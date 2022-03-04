import json

from django.http import (
    JsonResponse,
)
from django.shortcuts import (
    render,
)
from django.views import (
    View,
)
from recipes.models import CookStep, Recipe, RecipeProduct
from users.models import Author, CustomUser
from django.db.models import Count, Q, F, Value


class Task1View(View):
    """
    Вывести список всех рецептов. Элементом списка будет являться список, содержащий следующие значения:
        - Email автора;
        - Название рецепта;
        - Описание рецепта.
    """

    def get(self, request, **kwargs):
        recipes = list(Recipe.objects.all().values_list('userrecipe__user', 'title', 'description'))

        return JsonResponse(dict(recipes=recipes), json_dumps_params=dict(ensure_ascii=False))


class Task2View(View):
    """
    Вывести детальную информацию рецепта с идентификатором 1.
    Нужно получить информацию о шагах приготовления, списке необходимых продуктов для приготовления

    Шаги представляют собой список:
        - Название шага;
        - Описание шага.

    Продукты представляют собой список:
        - Название продукта;
        - Описание продукта;
        - Количество продукта;
        - Аббревиатура единицы измерения продукта.
    """

    def get(self, request, **kwargs):
        recipe = Recipe.objects.get(id=1)
        steps = list(CookStep.objects.values_list('title', 'description').filter(recipe=recipe))
        products = list(RecipeProduct.objects.values_list(
                'product__title',
                'product__description',
                'count',
                'unit__abbreviation'
            ).filter(recipe=recipe)
        )

        recipe_data = {
            'steps': steps,
            'products': products,
        }

        return JsonResponse(dict(recipe_data=recipe_data), json_dumps_params=dict(ensure_ascii=False, default=str))


class Task3View(View):
    """
    Вывести список рецептов, аналогичный заданию 1, только дополнительно должно быть выведено количество лайков. Сам
    список должен быть отсортирован по количеству лайков по убыванию.
    Элементом списка будет являться список, содержащий следующие значения:
        - Email автора;
        - Название рецепта;
        - Описание рецепта;
        - Количество лайков.
    """

    def get(self, request, **kwargs):
        recipes = list(Recipe.objects.all().annotate(
            like_count=Count(Q(vote__is_like=True))
        ).values_list('like_count', 'userrecipe__user', 'title', 'description').order_by('like_count'))

        return JsonResponse(dict(recipes=recipes), json_dumps_params=dict(ensure_ascii=False, default=str))


class Task4View(View):
    """
    Вывести списки TOP 3 авторов и TOP 3 голосующих с количеством рецептов для первых и количеством
    голосов для вторых. В выборке должен быть указан тип в отдельной колонке - Автор или Пользователь.

    Элементом списка авторов будет являться список, содержащий следующие значения:
        - Статус;
        - Email;
        - Количество рецептов.

    Элементом списка пользователей будет являться список, содержащий следующие значения:
        - Статус;
        - Email;
        - Количество лайков.

    """

    def get(self, request, **kwargs):
        authors = list(Author.objects.all().annotate(
            like_count=Count('userrecipe')).values_list(
            Value('Автор'),
            'email',
            'like_count',
        ).order_by('-like_count'))[:3]

        voters = list(CustomUser.objects.filter(author__isnull=True).annotate(
            like_count=Count('vote__recipe')).values_list(
            Value('Пользователь'),
            'email',
            'like_count',
        ).order_by('-like_count'))[:3]

        data = {
            'authors': authors,
            'voters': voters,
        }

        return JsonResponse(dict(data=data), json_dumps_params=dict(ensure_ascii=False, default=str))


class Task5View(View):
    """
    Все продукты указаны для приготовления одной порции блюда. Нужно вывести список необходимых продуктов для
    приготовления блюда с идентификатором 3 в количестве пяти порций.

    Элементом списка продуктов будет являться список, содержащий следующие значения:
        - Название рецепта;
        - Описание рецепта;
        - Название продукта;
        - Количество;
        - Аббревиатура единицы измерения.
    """

    def get(self, request, **kwargs):
        dish = Recipe.objects.get(id=3)
        recipe_products = list(RecipeProduct.objects.values_list(
            'recipe__title',
            'recipe__description',
            'product__title',
            (F('count')*5),
            'unit__abbreviation',
        ).filter(recipe=dish))

        return JsonResponse(
            data=dict(recipe_products=recipe_products), json_dumps_params=dict(ensure_ascii=False, default=str),
        )
