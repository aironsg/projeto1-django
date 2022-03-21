
from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class RecipeURLsTest(TestCase):
    def test_recipe_home_is_correct(self):
        url_home = reverse('recipes:home')
        self.assertEqual(url_home, '/')

    def test_recipe_category_is_correct(self):
        url_category = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url_category, '/recipes/category/1/')

    def test_recipe_recipe_is_correct(self):
        url_recipe = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url_recipe, '/recipes/1/')
