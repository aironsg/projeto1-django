
from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views

# Create your tests here.


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view_home = resolve(reverse('recipes:home'))
        self.assertIs(view_home.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view_category = resolve(
            reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view_category.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view_detail = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view_detail.func, views.recipe)
